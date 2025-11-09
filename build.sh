#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Verify installation
python3 -c "import snakeskin; print('Snakeskin installed successfully')"

# Build the project
python3 main.py

echo "Build completed successfully!"
