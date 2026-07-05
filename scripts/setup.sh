#!/bin/bash
set -euo pipefail
echo "Setting up Data Lineage Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
