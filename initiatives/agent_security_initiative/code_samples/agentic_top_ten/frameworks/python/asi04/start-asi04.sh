#!/bin/bash
set -e

echo "ASI-04 Lab - Starting..."
echo ""

docker-compose -f docker-compose-asi04.yml down 2>/dev/null || true
docker-compose -f docker-compose-asi04.yml up --build -d

echo ""
echo "✓ Lab running at http://localhost:5050"
echo ""
