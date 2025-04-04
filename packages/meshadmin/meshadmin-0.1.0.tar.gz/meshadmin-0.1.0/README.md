# Meshadmin
A simple admin interface for the nebula mesh.

Allows to administer multiple networks.

## Installation
###  Setup CLI on host
```bash
# Install Git and Curl
apt install git curl

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Source the environment
source $HOME/.local/bin/env

# Install Meshadmin
uv pip install meshadmin --index-url https://gitlab.com/api/v4/projects/61460862/packages/pypi/simple --system
```

### Usage
```bash
# Download Nebula binaries
meshadmin download

# Enroll a new host
meshadmin enroll ENROLLMENT_KEY

# Install as a service
meshadmin install-service

# Start service
meshadmin start-service

# Other commands
meshadmin --help
```
