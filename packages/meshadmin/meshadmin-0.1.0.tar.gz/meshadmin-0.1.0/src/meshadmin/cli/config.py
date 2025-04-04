import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class MeshConfig:
    server_url: str
    keycloak_base_url: str
    keycloak_realm: str
    keycloak_admin_client: str
    keycloak_issuer: str
    keycloak_device_auth_url: str
    keycloak_token_url: str
    api_endpoint: str
    private_key: Path
    private_net_key_file: Path
    public_net_key_file: Path
    config_path: Path
    authentication_path: Path
    systemd_service_path: Path
    meshadmin_etc_path: Path


def load_config():
    SERVER_URL = os.getenv("MESH_SERVER_URL", "http://dmeshadmin.hydo.ch")
    KEYCLOAK_BASE_URL = os.getenv(
        "KEYCLOAK_BASE_URL", "https://auth.dmeshadmin.hydo.ch"
    )
    KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "meshadmin")
    KEYCLOAK_ADMIN_CLIENT = os.getenv("KEYCLOAK_ADMIN_CLIENT", "admin-cli")
    KEYCLOAK_ISSUER = f"{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}"
    KEYCLOAK_DEVICE_AUTH_URL = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/auth/device"
    KEYCLOAK_TOKEN_URL = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/token"

    return MeshConfig(
        server_url=SERVER_URL,
        keycloak_base_url=KEYCLOAK_BASE_URL,
        keycloak_realm=KEYCLOAK_REALM,
        keycloak_admin_client=KEYCLOAK_ADMIN_CLIENT,
        keycloak_issuer=KEYCLOAK_ISSUER,
        keycloak_device_auth_url=KEYCLOAK_DEVICE_AUTH_URL,
        keycloak_token_url=KEYCLOAK_TOKEN_URL,
        api_endpoint=f"{SERVER_URL}/api/v1",
        private_key=Path("auth.key"),
        private_net_key_file=Path("host.key"),
        public_net_key_file=Path("host.pub"),
        config_path=Path("config.yaml"),
        authentication_path=Path("auth.json"),
        systemd_service_path=Path("/usr/lib/systemd/system/meshadmin.service"),
        meshadmin_etc_path=Path("/etc/meshadmin"),
    )
