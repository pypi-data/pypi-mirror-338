# Meshadmin
A simple admin interface for the nebula mesh.

Allows to administer multiple networks.

## Installation
###  Setup CLI on host
```bash
# Install Curl
apt install curl

# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to your current shell session
source $HOME/.local/bin/env

# Install meshadmin package
uv tool install meshadmin
```

### Usage
```bash
# Download Nebula binaries
meshadmin download

# Enroll a new host
meshadmin enroll --mesh-admin-endpoint <MESH_ADMIN_ENDPOINT> <ENROLLMENT_KEY>

# Start process for config updates
meshadmin start --mesh-admin-endpoint <MESH_ADMIN_ENDPOINT>

# Install as a service
meshadmin install-service --mesh-admin-endpoint <MESH_ADMIN_ENDPOINT>

# Start service
meshadmin start-service

# Other commands
meshadmin --help
```

### Configuration

The CLI supports the following environment variable:

- `MESH_ADMIN_ENDPOINT`: URL of the admin endpoint
