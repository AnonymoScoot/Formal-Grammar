#!/bin/bash

SCRIPT_DIR=$(readlink -f "$(dirname "$0")")
cd "$SCRIPT_DIR"
cd ..
python -m unittest discover
