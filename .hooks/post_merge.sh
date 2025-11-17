#!/bin/bash

# Get pre-merge hash from the target branch
old_hash=$(git show ORIG_HEAD:poetry.lock | md5sum 2> /dev/null || echo "")

# Get current hash
new_hash=$(md5sum poetry.lock 2> /dev/null || echo "")

# Compare and run poetry install if changed
if [ "$old_hash" != "$new_hash" ]; then
    echo "📦 Root dependencies changed. Running poetry install..."
    poetry install || {
        echo "❌ Failed to update dependencies"
        exit 1
    }
    echo "✅ Root dependencies updated!"
else
    echo "📦 No root dependency changes"
fi

# Get pre-merge hash from the target branch
old_hash=$(git show ORIG_HEAD:components/api/poetry.lock | md5sum 2> /dev/null || echo "")

# Get current hash
new_hash=$(md5sum components/api/poetry.lock 2> /dev/null || echo "")

# Compare and run poetry install if changed
if [ "$old_hash" != "$new_hash" ]; then
    echo "📦 API dependencies changed. Running poetry install..."
    cd components/api || exit
    if ! poetry install --with dev; then
        echo "❌ Failed to update dependencies"
        exit 1
    fi
    echo "✅ API dependencies updated!"
else
    echo "📦 No API dependency changes"
fi
