#!/bin/bash
set -e

echo "Testing ASI-04 Lab..."
echo ""

# Test  1: Switch to compromised
echo "1. Triggering compromise..."
curl -s -X POST http://localhost:5050/switch_registry > /dev/null
FLAG=$(curl -s http://localhost:5050/status | grep -o "ASI04_FLAG{[^}]*}")
echo "   Flag: $FLAG"

# Test 2: Enable mitigation
echo "2. Enabling mitigation..."
curl -s -X POST http://localhost:5050/toggle_mitigation > /dev/null
echo "   ✓ Provenance checking enabled"

# Test 3: Try switching (should block)
echo "3. Testing mitigation..."
curl -s -X POST http://localhost:5050/switch_registry > /dev/null
STATUS=$(curl -s http://localhost:5050/status | grep -o "evil-mcp" || echo "blocked")
if [ "$STATUS" = "blocked" ]; then
    echo "   ✓ Evil MCP blocked!"
else
    echo "   ✗ Evil MCP not blocked"
fi

echo ""
echo "✓ Tests complete"
echo ""
