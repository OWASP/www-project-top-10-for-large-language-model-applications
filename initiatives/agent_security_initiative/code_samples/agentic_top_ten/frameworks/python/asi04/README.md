# ASI-04: Supply Chain Compromise Lab

Hands-on lab demonstrating MCP registry poisoning and provenance-based mitigation.

## Quick Start

```bash
docker-compose -f docker-compose-asi04.yml up --build
```

Open browser: **http://localhost:5050**

## Lab Flow

### Phase 1: Demonstrate Attack
1. Click **🔄 Switch Registry**
2. See **COMPROMISED** warning + flag
3. Flag: `ASI04_FLAG{mcp_supply_chain_compromised}`

### Phase 2: Enable Mitigation
1. Click **🔄 Switch Registry** (revert to legit)
2. Click **🛡️ Toggle Provenance Checking**
3. Status → **ENABLED ✓**

### Phase 3: Test Mitigation
1. Click **🔄 Switch Registry** (try to load evil MCP)
2. **Agent REFUSES** - evil MCP blocked!
3. Check "Load Status Details" for block reason
4. ✓ Attack prevented

## What You'll Learn

- Supply chain attacks need no runtime exploits
- Registry poisoning is trivial without verification
- Provenance checking blocks untrusted code

## API Testing

```bash
# Check status
curl http://localhost:5050/status | jq .

# Enable mitigation
curl -X POST http://localhost:5050/toggle_mitigation | jq .

# Try switching (blocked if mitigation on)
curl -X POST http://localhost:5050/switch_registry | jq .
```

## Cleanup

```bash
docker-compose -f docker-compose-asi04.yml down
```
