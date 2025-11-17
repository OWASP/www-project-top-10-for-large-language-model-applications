#!/bin/bash
set -euo pipefail

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo 'Error: npm is not installed.' >&2
    exit 1
fi

# Check if Prettier is installed, install it if missing
if ! command -v prettier &> /dev/null; then
    echo 'Error: Prettier is not installed.' >&2
    echo 'Installing Prettier...'
    npm install -g prettier
fi

# Verify Prettier is installed
if ! command -v prettier &> /dev/null; then
    echo 'Error: Prettier installation failed.' >&2
    exit 1
fi

# Run Prettier on staged .json, .yaml, and .yml files
echo "Running Prettier on staged files..."

# List all staged files, filter for the desired extensions, and run Prettier
git diff --cached --name-only --diff-filter=d |
      grep -E '\.(json|ya?ml)$' |
      xargs -I {} prettier --write {}

# Add the files back to staging area as Prettier may have modified them
git diff --name-only --diff-filter=d |
      grep -E '\.(json|ya?ml)$' |
      xargs git add

echo "Prettier formatting completed."
exit 0
