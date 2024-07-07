#!/bin/bash

# MacOS

# Create private environment
python3 -m venv myenv

# Activate your environment

source myenv/bin/activate

# Install all required frameworks

pip3 install xmltodict
pip3 install pyyaml