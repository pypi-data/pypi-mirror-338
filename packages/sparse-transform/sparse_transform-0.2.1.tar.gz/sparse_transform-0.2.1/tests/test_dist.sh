#!/bin/bash
# This script tests the latest version of the sparse_transform package
# by creating a virtual environment, installing the package from the dist folder,
# and running the tests.
# Run it at project root with: `bash tests/test_dist.sh`

# Create a new Python virtual environment
python3 -mvenv test_venv

# Activate the virtual environment
source test_venv/bin/activate

# Install the latest version of the package from the dist folder
pip install "$(ls -t dist/sparse_transform-*.whl | head -n 1)"

# Run the tests only if the previous command succeeds
if [ $? -eq 0 ]; then
    python -m unittest discover -s tests
else
    echo "Package installation failed. Skipping tests."
    exit 1
fi

# Remove the virtual environment
rm -rf test_venv