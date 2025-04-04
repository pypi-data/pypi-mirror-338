import asyncio
import json
import os
import platform
import shutil
import signal
import subprocess
from datetime import datetime, timedelta
from importlib import resources
from pathlib import Path
from time import sleep
from typing import Annotated
from uuid import uuid4

import httpx
import jwt
import structlog
import typer
from jwcrypto.jwk import JWK
from jwcrypto.jwt import JWT
from jwt import decode
from rich import print, print_json

from meshadmin.cli.config import load_config
from meshadmin.cli.schemas import ClientEnrollment, NetworkCreate, TemplateCreate
from meshadmin.common.utils import (
    create_expiration_date,
    create_keys,
    download_nebula_binaries,
    get_nebula_path,
    get_public_ip,
)

app = typer.Typer()
logger = structlog.get_logger(__name__)
config = load_config()


@app.command()
def download():
    logger.info("Downloading nebula binaries")
    try:
        install_path = download_nebula_binaries(config.api_endpoint)
        logger.info("Nebula binaries downloaded successfully", path=str(install_path))
    except Exception as e:
        logger.error("Failed to download nebula binaries", error=str(e))
        raise typer.Exit(code=1)


@app.command()
def enroll(
    enrollment_key: Annotated[
        str,
        typer.Argument(envvar="MESH_ENROLLMENT_KEY"),
    ],
    preferred_hostname: Annotated[
        str,
        typer.Option(envvar="MESH_HOSTNAME"),
    ] = None,
    public_ip: Annotated[
        str,
        typer.Option(envvar="MESH_PUBLIC_IP"),
    ] = None,
    mesh_config_path: Annotated[
        Path,
        typer.Option(envvar="MESH_CONFIG_PATH"),
    ] = ".",
    mesh_admin_endpoint: Annotated[
        str,
        typer.Option(envvar="MESH_ADMIN_ENDPOINT"),
    ] = config.server_url,
):
    logger.info("enrolling")

    if not mesh_config_path.exists():
        mesh_config_path.mkdir(exist_ok=True, parents=True)

    private_auth_key_path = mesh_config_path / config.private_key
    if private_auth_key_path.exists():
        logger.info("auth key already exists")
    else:
        logger.info("creating auth key")
        create_auth_key(mesh_config_path)

    jwk = JWK.from_json(private_auth_key_path.read_text())
    public_auth_key = jwk.export_public()
    logger.info("public key for registration", public_key=public_auth_key)

    private_net_key_path = mesh_config_path / config.private_net_key_file
    public_net_key_path = mesh_config_path / config.public_net_key_file

    if public_ip is None:
        public_ip = get_public_ip()
        logger.info(
            "public ip not set, using ip reported by https://checkip.amazonaws.com/",
            public_ip=public_ip,
        )

    if preferred_hostname is None:
        preferred_hostname = platform.node()
        logger.info(
            "preferred hostname not set, using system hostname",
            hostname=preferred_hostname,
        )

    if private_net_key_path.exists() and public_net_key_path.exists():
        public_nebula_key = public_net_key_path.read_text()
        logger.info(
            "private and public nebula key already exists",
            public_key=public_nebula_key,
        )
    else:
        logger.info("creating private and public nebula key")
        private, public_nebula_key = create_keys()
        private_net_key_path.write_text(private)
        private_auth_key_path.chmod(0o600)
        public_net_key_path.write_text(public_nebula_key)
        public_net_key_path.chmod(0o600)
        logger.info(
            "private and public nebula key created", public_nebula_key=public_nebula_key
        )

    enrollment = ClientEnrollment(
        enrollment_key=enrollment_key,
        public_net_key=public_nebula_key,
        public_auth_key=public_auth_key,
        preferred_hostname=preferred_hostname,
        public_ip=public_ip,
    )

    res = httpx.post(
        f"{mesh_admin_endpoint}/api/v1/enroll",
        content=enrollment.model_dump_json(),
        headers={"Content-Type": "application/json"},
    )
    res.raise_for_status()

    get_config(mesh_config_path, mesh_admin_endpoint)
    logger.info("enrollment response", enrollment=res.content)
    logger.info("enrollment finished")


@app.command()
def install_service(
    mesh_config_path: Annotated[
        Path,
        typer.Option(envvar="MESH_CONFIG_PATH"),
    ] = None,
    mesh_admin_endpoint: Annotated[
        str,
        typer.Option(envvar="MESH_ADMIN_ENDPOINT"),
    ] = config.server_url,
):
    os_name = platform.system()
    meshadmin_path = shutil.which("meshadmin")

    if not meshadmin_path:
        logger.error("meshadmin executable not found in PATH")
        exit(1)

    if mesh_config_path is None:
        if os_name == "Darwin":
            mesh_config_path = Path(
                os.path.expanduser("~/Library/Application Support/meshadmin")
            )
        else:
            mesh_config_path = Path("/etc/meshadmin")

    mesh_config_path = Path(os.path.expanduser(str(mesh_config_path)))
    if not mesh_config_path.exists():
        mesh_config_path.mkdir(exist_ok=True, parents=True)

    (mesh_config_path / "env").write_text(
        f"""MESH_ADMIN_ENDPOINT={mesh_admin_endpoint}
        MESH_CONFIG_PATH={mesh_config_path.absolute()}
        """
    )
    if os_name == "Darwin":
        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.meshadmin.service</string>
    <key>ProgramArguments</key>
    <array>
        <string>{meshadmin_path}</string>
        <string>start</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>MESH_ADMIN_ENDPOINT</key>
        <string>{mesh_admin_endpoint}</string>
        <key>MESH_CONFIG_PATH</key>
        <string>{mesh_config_path.absolute()}</string>
    </dict>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>{mesh_config_path.absolute()}/error.log</string>
    <key>StandardOutPath</key>
    <string>{mesh_config_path.absolute()}/output.log</string>
</dict>
</plist>
"""
        launch_agents_dir = Path(os.path.expanduser("~/Library/LaunchAgents"))
        if not launch_agents_dir.exists():
            launch_agents_dir.mkdir(exist_ok=True, parents=True)
        plist_path = launch_agents_dir / "com.meshadmin.service.plist"
        plist_path.write_text(plist_content)
        subprocess.run(["launchctl", "load", str(plist_path)])
        logger.info(
            "meshadmin service installed and started",
            plist_path=str(plist_path),
            config_path=str(mesh_config_path),
        )
        print(f"meshadmin service installed at {plist_path}")
        print(f"Configuration directory: {mesh_config_path}")
        print("Service has been loaded and will start automatically on login")

    else:
        systemd_unit = f"""[Unit]
Description=Meshadmin
Wants=basic.target network-online.target nss-lookup.target time-sync.target
After=basic.target network.target network-online.target
Before=sshd.service

[Service]
#Type=notify
#NotifyAccess=main
SyslogIdentifier=meshadmin
EnvironmentFile={mesh_config_path.absolute()}/env
ExecReload=/bin/kill -HUP $MAINPID
ExecStart={meshadmin_path} start 
Restart=always

[Install]
WantedBy=multi-user.target
"""
        config.systemd_service_path.write_text(systemd_unit)
        subprocess.run(["systemctl", "daemon-reload"])
        subprocess.run(["systemctl", "enable", "meshadmin"])
        print(f"meshadmin service installed at {config.systemd_service_path}")
        print(f"Configuration directory: {mesh_config_path}")
        print("Service has been enabled and will start automatically on boot")


@app.command()
def uninstall_service():
    os_name = platform.system()
    if os_name == "Darwin":
        plist_path = Path(
            os.path.expanduser("~/Library/LaunchAgents/com.meshadmin.service.plist")
        )
        if plist_path.exists():
            subprocess.run(["launchctl", "unload", str(plist_path)])
            plist_path.unlink()
            logger.info("meshadmin service uninstalled", plist_path=str(plist_path))
            print(f"meshadmin service uninstalled from {plist_path}")
        else:
            logger.warning("meshadmin service not found", plist_path=str(plist_path))
            print("meshadmin service not found, nothing to uninstall")
    else:
        if config.systemd_service_path.exists():
            subprocess.run(["systemctl", "stop", "meshadmin"])
            subprocess.run(["systemctl", "disable", "meshadmin"])
            subprocess.run(["systemctl", "daemon-reload"])
            config.systemd_service_path.unlink()
            env_path = Path("/etc/meshadmin/env")
            if env_path.exists():
                env_path.unlink()
            logger.info("meshadmin service uninstalled")
            print("meshadmin service uninstalled")
        else:
            logger.warning("meshadmin service not found")
            print("meshadmin service not found, nothing to uninstall")


@app.command()
def start_service():
    os_name = platform.system()
    if os_name == "Darwin":
        plist_path = Path(
            os.path.expanduser("~/Library/LaunchAgents/com.meshadmin.service.plist")
        )
        if plist_path.exists():
            subprocess.run(["launchctl", "load", str(plist_path)])
            logger.info("meshadmin service started")
            print("meshadmin service started")
        else:
            logger.error("meshadmin service not installed", plist_path=str(plist_path))
            print(
                "meshadmin service not installed. Run 'meshadmin install_service' first."
            )
    else:
        subprocess.run(["systemctl", "start", "meshadmin"])
        print("meshadmin service started")


@app.command()
def stop_service():
    os_name = platform.system()
    if os_name == "Darwin":
        plist_path = Path(
            os.path.expanduser("~/Library/LaunchAgents/com.meshadmin.service.plist")
        )
        if plist_path.exists():
            subprocess.run(["launchctl", "unload", str(plist_path)])
            logger.info("meshadmin service stopped")
            print("meshadmin service stopped")
        else:
            logger.error("meshadmin service not installed", plist_path=str(plist_path))
            print("meshadmin service not installed. Nothing to stop.")
    else:
        subprocess.run(["systemctl", "stop", "meshadmin"])
        print("meshadmin service stopped")


@app.command()
def create_auth_key(
    mesh_config_path: Annotated[
        Path,
        typer.Argument(envvar="MESH_CONFIG_PATH"),
    ] = ".",
):
    jwk = JWK.generate(kty="RSA", kid=str(uuid4()), size=2048)
    auth_key = mesh_config_path / config.private_key
    auth_key.write_text(jwk.export_private())
    auth_key.chmod(0o600)


@app.command()
def show_auth_public_key(
    mesh_config_path: Annotated[
        Path,
        typer.Argument(envvar="MESH_CONFIG_PATH"),
    ] = ".",
):
    jwk = JWK.from_json((mesh_config_path / config.private_key).read_text())
    print(jwk.export_public())


@app.command()
def create_net_keys(
    mesh_config_path: Annotated[
        Path,
        typer.Argument(envvar="MESH_CONFIG_PATH"),
    ] = ".",
):
    private, public = create_keys()
    private_net_key_path = mesh_config_path / config.private_net_key_file
    private_net_key_path.write_text(private)
    private_net_key_path.chmod(0o600)
    public_net_key_path = mesh_config_path / config.public_net_key_file
    public_net_key_path.write_text(public)
    public_net_key_path.chmod(0o600)


@app.command()
def get_config(
    mesh_config_path: Annotated[
        Path,
        typer.Option(envvar="MESH_CONFIG_PATH"),
    ] = ".",
    mesh_admin_endpoint: Annotated[
        str,
        typer.Option(envvar="MESH_ADMIN_ENDPOINT"),
    ] = config.server_url,
):
    private_net_key, public_net_key = create_keys()
    private_auth_key = JWK.from_json(
        (mesh_config_path / config.private_key).read_text()
    )

    loop = asyncio.get_event_loop()

    result, _ = loop.run_until_complete(
        get_config_from_mesh(mesh_admin_endpoint, private_auth_key)
    )
    (mesh_config_path / config.config_path).write_text(result)


async def get_config_from_mesh(mesh_admin_endpoint, private_auth_key):
    jwt = JWT(
        header={"alg": "RS256", "kid": private_auth_key.thumbprint()},
        claims={
            "exp": create_expiration_date(10),
            "kid": private_auth_key.thumbprint(),
        },
    )
    jwt.make_signed_token(private_auth_key)
    token = jwt.serialize()

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{mesh_admin_endpoint}/api/v1/config",
            headers={"Authorization": f"Bearer {token}"},
        )
        res.raise_for_status()
        config = res.text
        update_interval = int(res.headers.get("X-Update-Interval", "5"))
        return config, update_interval


async def cleanup_ephemeral_hosts(mesh_admin_endpoint, private_auth_key):
    jwt_token = JWT(
        header={"alg": "RS256", "kid": private_auth_key.thumbprint()},
        claims={
            "exp": create_expiration_date(10),
            "kid": private_auth_key.thumbprint(),
        },
    )
    jwt_token.make_signed_token(private_auth_key)
    token = jwt_token.serialize()

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{mesh_admin_endpoint}/api/v1/cleanup-ephemeral",
            headers={"Authorization": f"Bearer {token}"},
        )
        res.raise_for_status()
        return res.json()


async def start_nebula(mesh_config_path, mesh_admin_endpoint):
    await logger.ainfo("starting nebula")
    conf_path = mesh_config_path / config.config_path
    assert conf_path.exists(), f"Config at {conf_path} does not exist"

    private_auth_key_path = mesh_config_path / config.private_key
    assert private_auth_key_path.exists(), (
        f"private_key at {private_auth_key_path} does not exist"
    )

    async def start_process():
        return await asyncio.create_subprocess_exec(
            get_nebula_path(),
            "-config",
            str(conf_path),
            cwd=mesh_config_path,
        )

    proc = await start_process()

    # Default update interval in seconds
    update_interval = 5

    while True:
        await asyncio.sleep(update_interval)
        try:
            private_auth_key_path = mesh_config_path / config.private_key
            private_auth_key = JWK.from_json(private_auth_key_path.read_text())

            # Check for config updates
            try:
                new_config, new_update_interval = await get_config_from_mesh(
                    mesh_admin_endpoint, private_auth_key
                )

                if update_interval != new_update_interval:
                    await logger.ainfo(
                        "update interval changed",
                        old_interval=update_interval,
                        new_interval=new_update_interval,
                    )
                    update_interval = new_update_interval

                old_config = conf_path.read_text()
                if new_config != old_config:
                    await logger.ainfo("config changed, reloading")
                    conf_path.write_text(new_config)
                    conf_path.chmod(0o600)

                    try:
                        proc.send_signal(signal.SIGHUP)
                    except ProcessLookupError:
                        await logger.ainfo("process died, restarting")
                        proc = await start_process()
                else:
                    await logger.ainfo("config not changed")
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    await logger.aerror(
                        "Could not get config because of authentication error. Host may have been deleted.",
                        error=str(e),
                        response_text=e.response.text,
                    )
                    print(
                        "Error: Could not get config because of authentication error. Host may have been deleted."
                    )
                    print(f"Server message: {e.response.text}")
                    break
                else:
                    await logger.aerror("error getting config", error=str(e))

            # Cleanup ephemeral hosts
            try:
                result = await cleanup_ephemeral_hosts(
                    mesh_admin_endpoint, private_auth_key
                )
                if result.get("removed_count", 0) > 0:
                    await logger.ainfo(
                        "removed stale ephemeral hosts",
                        count=result["removed_count"],
                    )
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    await logger.aerror(
                        "Could not clean up ephemeral hosts because of authentication error. Host may have been deleted.",
                        error=str(e),
                        response_text=e.response.text,
                    )
                    print(
                        "Error: Could not clean up ephemeral hosts because of authentication error. Host may have been deleted."
                    )
                    print(f"Server message: {e.response.text}")
                    break
                else:
                    await logger.aerror("error during cleanup operation", error=str(e))

        except Exception:
            await logger.aexception("could not refresh token")
            if proc.returncode is not None:
                await logger.ainfo("process died, restarting")
                proc = await start_process()

    # Clean shutdown if we get here
    if proc.returncode is None:
        await logger.ainfo("shutting down nebula process")
        proc.terminate()
        try:
            await asyncio.wait_for(proc.wait(), timeout=5.0)
        except asyncio.TimeoutError:
            await logger.awarning("nebula process didn't terminate, killing it")
            proc.kill()


@app.command()
def start(
    mesh_config_path: Annotated[
        Path,
        typer.Option(envvar="MESH_CONFIG_PATH"),
    ] = ".",
    mesh_admin_endpoint: Annotated[
        str,
        typer.Option(envvar="MESH_ADMIN_ENDPOINT"),
    ] = config.server_url,
):
    asyncio.run(start_nebula(mesh_config_path, mesh_admin_endpoint))


@app.command()
def show_public_key(private_key: Path):
    jwk = JWK.from_json(private_key.read_text())
    print(jwk.export_public())


@app.command()
def login():
    res = httpx.post(
        config.keycloak_device_auth_url,
        data={
            "client_id": config.keycloak_admin_client,
        },
    )
    res.raise_for_status()

    device_auth_response = res.json()
    print(device_auth_response)
    print(
        "Please open the verification url",
        device_auth_response["verification_uri_complete"],
    )

    while True:
        res = httpx.post(
            config.keycloak_token_url,
            data={
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                "client_id": config.keycloak_admin_client,
                "device_code": device_auth_response["device_code"],
            },
        )
        if res.status_code == 200:
            logger.info("Received auth token")
            config.authentication_path.write_bytes(res.content)
            config.authentication_path.chmod(0o600)

            access_token = res.json()["access_token"]
            refresh_token = res.json()["refresh_token"]
            print(
                jwt.decode(
                    refresh_token,
                    algorithms=["RS256"],
                    options={"verify_signature": False},
                )
            )
            logger.info("access_token", access_token=access_token)
            print("successfully authenticated")
            break
        else:
            print(res.json())
        sleep(device_auth_response["interval"])


def get_access_token():
    if config.authentication_path.exists():
        auth = json.loads(config.authentication_path.read_text())
        access_token = auth["access_token"]

        decoded_token = decode(
            access_token, options={"verify_signature": False, "verify_exp": False}
        )

        # is exp still 2/3 of the time
        if decoded_token["exp"] >= (datetime.now() + timedelta(seconds=10)).timestamp():
            return access_token
        else:
            refresh_token = auth["refresh_token"]
            res = httpx.post(
                config.keycloak_token_url,
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": refresh_token,
                    "client_id": config.keycloak_admin_client,
                },
            )
            res.raise_for_status()
            config.authentication_path.write_bytes(res.content)
            return res.json()["access_token"]

    else:
        print("authentication failed")


@app.command()
def create_network(name: str, cidr: str):
    try:
        access_token = get_access_token()
    except Exception:
        logger.exception("failed to get access token")
        exit(1)

    res = httpx.post(
        f"{config.api_endpoint}/networks",
        content=NetworkCreate(name=name, cidr=cidr).model_dump_json(),
        headers={"Authorization": f"Bearer {access_token}"},
    )

    if res.status_code >= 400:
        print("could not create network:", res.text)
        exit(1)

    print_json(res.content.decode("utf-8"))


@app.command()
def list_networks():
    try:
        access_token = get_access_token()
    except Exception:
        logger.exception("failed to get access token")
        exit(1)

    res = httpx.get(
        f"{config.api_endpoint}/networks",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    res.raise_for_status()
    print(res.json())


@app.command()
def create_template(
    name: str, network_name: str, is_lighthouse: bool, is_relay: bool, use_relay: bool
):
    try:
        access_token = get_access_token()
    except Exception:
        logger.exception("failed to get access token")
        exit(1)

    res = httpx.post(
        f"{config.api_endpoint}/templates",
        content=TemplateCreate(
            name=name,
            network_name=network_name,
            is_lighthouse=is_lighthouse,
            is_relay=is_relay,
            use_relay=use_relay,
        ).model_dump_json(),
        headers={"Authorization": f"Bearer {access_token}"},
    )
    res.raise_for_status()
    print_json(res.content.decode("utf-8"))


@app.command()
def delete_template(name: str):
    try:
        access_token = get_access_token()
    except Exception:
        logger.exception("failed to get access token")
        exit(1)

    res = httpx.delete(
        f"{config.api_endpoint}/templates/{name}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    res.raise_for_status()
    print(res.json())


@app.command()
def delete_host(name: str):
    try:
        access_token = get_access_token()
    except Exception:
        logger.exception("failed to get access token")
        exit(1)

    res = httpx.delete(
        f"{config.api_endpoint}/hosts/{name}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    res.raise_for_status()
    print(res.json())


@app.command()
def nebula_cert():
    binary_name = "nebula-cert"
    with resources.path("meshadmin.assets", binary_name) as binary_path:
        if not os.access(binary_path, os.X_OK):
            raise PermissionError(f"{binary_path} is not executable.")
        result = subprocess.run([binary_path, "--help"], text=True, capture_output=True)
        print(result.stdout)


if __name__ == "__main__":
    app()
