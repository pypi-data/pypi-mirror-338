import ipaddress

from meshadmin.cli.main import get_public_ip


def test_get_public_ip():
    public_ip = get_public_ip()
    ipaddress.ip_address(public_ip)
