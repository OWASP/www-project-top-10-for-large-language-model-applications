"""
ASI-04 Lab - Simple Agent
Loads MCP tools from registry and provides a simple web interface

This agent demonstrates ASI-04 vulnerability:
- Loads MCP endpoints from mcp_registry.json
- No signature verification
- No provenance checking
- Trusts registry implicitly
"""

import json
import os
import logging
from aiohttp import web
import aiohttp
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REGISTRY_FILE = os.getenv("REGISTRY_FILE", "/app/mcp_registry.json")
FLAG_ASI04 = os.getenv("FLAG_ASI04", "ASI04_FLAG{mcp_supply_chain_compromised}")


class SimpleAgent:
    """Simple agent that loads MCP tools from a registry"""

    def __init__(self):
        self.mcp_endpoints = {}
        self.tools = {}
        self.load_status = []
        self.mitigation_enabled = False
        self.trusted_sources = [
            "http://legit-mcp:5001"  # Allowlist of trusted MCP endpoints
        ]

    def load_registry(self):
        """Load MCP registry - VULNERABLE: No verification (unless mitigation enabled)"""
        try:
            with open(REGISTRY_FILE, 'r') as f:
                registry_data = json.load(f)

            logger.info(f"[Agent] Loaded MCP registry from {REGISTRY_FILE}")
            logger.info(f"[Agent] Found {len(registry_data)} MCP endpoints")

            # Clear previous endpoints and status
            self.mcp_endpoints = {}
            self.load_status = []

            for name, url in registry_data.items():
                # MITIGATION: Check provenance if enabled
                if self.mitigation_enabled:
                    if url not in self.trusted_sources:
                        logger.warning(f"[MITIGATION] Blocked untrusted MCP: {name} from {url}")
                        logger.warning(f"[MITIGATION] URL not in allowlist: {self.trusted_sources}")
                        self.load_status.append({
                            "name": name,
                            "url": url,
                            "loaded": False,
                            "blocked_reason": "Untrusted source - not in allowlist",
                            "timestamp": datetime.utcnow().isoformat()
                        })
                        continue  # Skip loading this MCP

                # Load the MCP endpoint
                self.mcp_endpoints[name] = url
                self.load_status.append({
                    "name": name,
                    "url": url,
                    "loaded": True,
                    "timestamp": datetime.utcnow().isoformat()
                })
                logger.info(f"[Agent] Loaded MCP: {name} from {url}")

            if self.mitigation_enabled:
                logger.info(f"[MITIGATION] Provenance check complete. Loaded {len(self.mcp_endpoints)} trusted MCPs")

            return True

        except Exception as e:
            logger.error(f"[Agent] Failed to load registry: {e}")
            return False

    async def discover_tools(self):
        """Discover tools from MCP endpoints - VULNERABLE: Trusts all tools"""
        for mcp_name, mcp_url in self.mcp_endpoints.items():
            try:
                async with aiohttp.ClientSession() as session:
                    # Call MCP list_tools endpoint
                    async with session.post(
                        f"{mcp_url}/mcp/list_tools",
                        json={},
                        timeout=aiohttp.ClientTimeout(total=10)
                    ) as response:
                        if response.status == 200:
                            data = await response.json()
                            tools = data.get("tools", [])

                            for tool in tools:
                                tool_name = tool.get("name")
                                self.tools[tool_name] = {
                                    "mcp_source": mcp_name,
                                    "mcp_url": mcp_url,
                                    "definition": tool
                                }

                            logger.info(f"[Agent] Discovered {len(tools)} tools from {mcp_name}")

            except Exception as e:
                logger.error(f"[Agent] Failed to discover tools from {mcp_name}: {e}")

    async def call_tool(self, tool_name: str, arguments: dict):
        """Call a tool via its MCP endpoint"""
        if tool_name not in self.tools:
            return {"error": f"Unknown tool: {tool_name}"}

        tool_info = self.tools[tool_name]
        mcp_url = tool_info["mcp_url"]

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{mcp_url}/mcp/call_tool",
                    json={"name": tool_name, "arguments": arguments},
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        return {"error": f"Tool call failed: {response.status}"}

        except Exception as e:
            logger.error(f"[Agent] Tool call failed: {e}")
            return {"error": str(e)}


# Create agent instance
agent = SimpleAgent()


# HTTP Handlers
async def handle_status(request):
    """Status endpoint showing agent configuration"""
    return web.json_response({
        "status": "running",
        "registry_file": REGISTRY_FILE,
        "mcp_endpoints": agent.mcp_endpoints,
        "load_status": agent.load_status,
        "tools_count": len(agent.tools),
        "tools": list(agent.tools.keys()),
        "mitigation_enabled": agent.mitigation_enabled,
        "trusted_sources": agent.trusted_sources if agent.mitigation_enabled else None,
        "vulnerability": "ASI-04: No MCP signature verification" if not agent.mitigation_enabled else "MITIGATED: Provenance checking enabled",
        "flag": FLAG_ASI04 if "evil-mcp" in str(agent.mcp_endpoints) else "Not compromised"
    })

async def handle_tools(request):
    """List all available tools"""
    tools_detail = {}
    for name, info in agent.tools.items():
        tools_detail[name] = {
            "source": info["mcp_source"],
            "description": info["definition"].get("description", "")
        }

    return web.json_response({
        "tools": tools_detail
    })

async def handle_execute(request):
    """Execute a tool"""
    try:
        body = await request.json()
        tool_name = body.get("tool")
        arguments = body.get("arguments", {})

        if not tool_name:
            return web.json_response({"error": "Missing 'tool' parameter"}, status=400)

        result = await agent.call_tool(tool_name, arguments)

        return web.json_response({
            "tool": tool_name,
            "arguments": arguments,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })

    except Exception as e:
        logger.error(f"Execute error: {e}")
        return web.json_response({"error": str(e)}, status=500)

async def handle_switch_registry(request):
    """Switch between legitimate and poisoned registry"""
    try:
        # Check which registry to switch to
        current_file = agent.mcp_endpoints

        if "legit-mcp:5001" in str(current_file):
            # Currently using legit, switch to poisoned
            new_registry = "/app/mcp_registry_poisoned.json"
            target = "poisoned (evil-mcp:5002)"
        else:
            # Currently using poisoned, switch to legit
            new_registry = "/app/mcp_registry.json"
            target = "legitimate (legit-mcp:5001)"

        # Update the registry file and reinitialize
        global REGISTRY_FILE
        REGISTRY_FILE = new_registry

        # Reload registry
        agent.load_registry()
        await agent.discover_tools()

        logger.warning(f"[Agent] Registry switched to: {target}")

        return web.json_response({
            "status": "switched",
            "message": f"Agent now using {target} registry",
            "registry_file": new_registry,
            "mcp_endpoints": agent.mcp_endpoints,
            "flag": FLAG_ASI04 if "evil-mcp" in str(agent.mcp_endpoints) else "Not compromised"
        })

    except Exception as e:
        logger.error(f"[Agent] Failed to switch registry: {e}")
        return web.json_response({
            "status": "error",
            "message": str(e)
        }, status=500)

async def handle_toggle_mitigation(request):
    """Toggle provenance checking mitigation on/off"""
    try:
        # Toggle mitigation state
        agent.mitigation_enabled = not agent.mitigation_enabled

        logger.warning(f"[MITIGATION] Provenance checking {'ENABLED' if agent.mitigation_enabled else 'DISABLED'}")

        # Reload registry with new mitigation setting
        agent.load_registry()
        await agent.discover_tools()

        blocked_mcps = [s for s in agent.load_status if not s.get("loaded", False)]

        return web.json_response({
            "status": "toggled",
            "mitigation_enabled": agent.mitigation_enabled,
            "message": f"Provenance checking {'enabled' if agent.mitigation_enabled else 'disabled'}",
            "trusted_sources": agent.trusted_sources,
            "mcp_endpoints": agent.mcp_endpoints,
            "tools_count": len(agent.tools),
            "blocked_mcps": blocked_mcps if agent.mitigation_enabled else [],
            "security_status": "PROTECTED" if agent.mitigation_enabled else "VULNERABLE"
        })

    except Exception as e:
        logger.error(f"[MITIGATION] Failed to toggle: {e}")
        return web.json_response({
            "status": "error",
            "message": str(e)
        }, status=500)

async def handle_index(request):
    """Simple web interface - rewritten for reliability"""

    # Get current status directly
    status_data = {
        "status": "running",
        "registry_file": REGISTRY_FILE,
        "mcp_endpoints": agent.mcp_endpoints,
        "load_status": agent.load_status,
        "tools_count": len(agent.tools),
        "tools": list(agent.tools.keys()),
        "mitigation_enabled": agent.mitigation_enabled,
        "trusted_sources": agent.trusted_sources if agent.mitigation_enabled else None,
        "vulnerability": "ASI-04: No MCP signature verification" if not agent.mitigation_enabled else "MITIGATED: Provenance checking enabled",
        "flag": FLAG_ASI04 if "evil-mcp" in str(agent.mcp_endpoints) else "Not compromised",
        "compromised": "evil-mcp" in str(agent.mcp_endpoints)
    }

    # Build HTML with server-side rendering
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>ASI-04 Supply Chain Compromise Lab</title>
    <meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache">
    <style>
        body {{
            font-family: 'Courier New', monospace;
            max-width: 1400px;
            margin: 20px auto;
            padding: 20px;
            background: #0a0a0a;
            color: #00ff00;
        }}
        .container {{
            border: 2px solid #00ff00;
            padding: 20px;
            border-radius: 5px;
        }}
        h1 {{ color: #00ff00; margin-bottom: 5px; }}
        h2 {{ color: #00ff00; margin-top: 5px; font-size: 1.2em; }}
        .card {{
            background: #1a1a1a;
            padding: 15px;
            margin: 15px 0;
            border-left: 4px solid #00ff00;
            border-radius: 3px;
        }}
        .btn {{
            background: #0a0a0a;
            color: #00ff00;
            border: 2px solid #00ff00;
            padding: 12px 24px;
            margin: 5px 5px 5px 0;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            border-radius: 3px;
        }}
        .btn:hover {{ background: #00ff00; color: #0a0a0a; }}
        .warning {{ color: #ff0000; font-weight: bold; }}
        .success {{ color: #00ff00; font-weight: bold; }}
        .info {{ color: #00aaff; }}
        pre {{ background: #0a0a0a; padding: 10px; overflow-x: auto; border: 1px solid #333; }}
        .status-badge {{
            display: inline-block;
            padding: 5px 10px;
            margin: 5px 0;
            border-radius: 3px;
            font-weight: bold;
        }}
        .vulnerable {{ background: #ff0000; color: #000; }}
        .protected {{ background: #00ff00; color: #000; }}
        .compromised {{ background: #ff9900; color: #000; }}
        code {{ background: #1a1a1a; padding: 2px 6px; border-radius: 3px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔐 ASI-04: Supply Chain Compromise Lab</h1>
        <h2>Agent Control Panel</h2>

        <!-- Status Card -->
        <div class="card">
            <h3>📊 Current Status</h3>
            <p><strong>Registry:</strong> <code>{REGISTRY_FILE}</code></p>
            <p><strong>MCP Endpoint:</strong> <code>{list(agent.mcp_endpoints.values())[0] if agent.mcp_endpoints else 'None'}</code></p>
            <p><strong>Tools Loaded:</strong> {len(agent.tools)}</p>
            <p><strong>Mitigation:</strong>
                {'<span class="status-badge protected">ENABLED ✓</span>' if agent.mitigation_enabled else '<span class="status-badge vulnerable">DISABLED ✗</span>'}
            </p>
            {f'<p class="warning">⚠️ COMPROMISED! Evil MCP detected!</p><p class="warning">🚩 Flag: {FLAG_ASI04}</p>' if status_data['compromised'] else '<p class="success">✓ Using legitimate MCP</p>'}
        </div>

        <!-- Demo Controls -->
        <div class="card">
            <h3>🎮 Demo Controls</h3>
            <form action="/switch_registry" method="POST" style="display: inline;">
                <button type="submit" class="btn">🔄 Switch Registry</button>
            </form>
            <form action="/toggle_mitigation" method="POST" style="display: inline;">
                <button type="submit" class="btn">🛡️ Toggle Provenance Checking</button>
            </form>
            <button onclick="location.reload()" class="btn">🔃 Refresh Page</button>
        </div>

        <!-- Mitigation Status -->
        <div class="card">
            <h3>🛡️ Provenance Checking Status</h3>
            {'<p class="success">✓ Provenance Checking: <strong>ENABLED</strong></p>' if agent.mitigation_enabled else '<p class="warning">✗ Provenance Checking: <strong>DISABLED</strong></p>'}
            {'<p class="warning">⚠️ Agent is VULNERABLE to supply chain attacks!</p>' if not agent.mitigation_enabled else '<p class="success">✓ Agent will block untrusted MCPs</p>'}
            {f'<p><strong>Trusted Sources:</strong></p><pre>{json.dumps(agent.trusted_sources, indent=2)}</pre>' if agent.mitigation_enabled else ''}
            {f'<p class="warning">⚠️ Blocked {len([s for s in agent.load_status if not s.get("loaded", False)])} untrusted MCP(s)</p>' if agent.mitigation_enabled and any(not s.get("loaded", False) for s in agent.load_status) else ''}
        </div>

        <!-- Tools -->
        <div class="card">
            <h3>🔧 Available Tools ({len(agent.tools)})</h3>
            {''.join([f'<div style="background: #0a0a0a; padding: 10px; margin: 5px 0; border: 1px solid #333;"><strong>{name}</strong><br>Source: {info["mcp_source"]}<br>{info["definition"].get("description", "")}</div>' for name, info in agent.tools.items()]) if agent.tools else '<p>No tools loaded</p>'}
        </div>

        <!-- Load Status Details -->
        <div class="card">
            <h3>📋 Load Status Details</h3>
            <pre>{json.dumps(agent.load_status, indent=2)}</pre>
        </div>

        <!-- Instructions -->
        <div class="card">
            <h3>📖 Demo Instructions</h3>
            <p><strong>Phase 1: Demonstrate Attack</strong></p>
            <ol>
                <li>Click <code>🔄 Switch Registry</code> to load the poisoned registry</li>
                <li>Observe the <span class="warning">COMPROMISED</span> warning appear</li>
                <li>Capture the flag: <code>{FLAG_ASI04}</code></li>
                <li>Check <a href="http://localhost:8666/dashboard" target="_blank">http://localhost:8666/dashboard</a> for exfiltrated data</li>
            </ol>

            <p><strong>Phase 2: Enable Mitigation</strong></p>
            <ol>
                <li>Click <code>🔄 Switch Registry</code> to revert to legitimate MCP</li>
                <li>Click <code>🛡️ Toggle Provenance Checking</code> to enable mitigation</li>
                <li>Observe status change to <span class="protected">ENABLED</span></li>
            </ol>

            <p><strong>Phase 3: Test Mitigation</strong></p>
            <ol>
                <li>Click <code>🔄 Switch Registry</code> to attempt loading poisoned registry</li>
                <li>🎯 <strong>Agent REFUSES to load untrusted MCP!</strong></li>
                <li>Check "Load Status Details" - evil MCP blocked with reason</li>
                <li>Supply chain attack prevented!</li>
            </ol>
        </div>

        <!-- API Endpoints -->
        <div class="card">
            <h3>🌐 API Endpoints</h3>
            <p><code>GET /status</code> - Get agent status</p>
            <p><code>POST /switch_registry</code> - Switch between legitimate and poisoned registry</p>
            <p><code>POST /toggle_mitigation</code> - Enable/disable provenance checking</p>
            <p><code>POST /execute</code> - Execute a tool</p>

            <p style="margin-top: 15px;"><strong>Example curl commands:</strong></p>
            <pre>curl http://localhost:5050/status | jq .
curl -X POST http://localhost:5050/toggle_mitigation | jq .
curl -X POST http://localhost:5050/switch_registry | jq .</pre>
        </div>
    </div>
</body>
</html>"""

    return web.Response(text=html, content_type='text/html')


async def on_startup(app):
    """Initialize agent on startup"""
    logger.info("=" * 60)
    logger.info("ASI-04 Agent Starting")
    logger.info("=" * 60)

    # Load registry
    if agent.load_registry():
        # Discover tools from MCP endpoints
        await agent.discover_tools()
        logger.info(f"[Agent] Ready with {len(agent.tools)} tools")
    else:
        logger.error("[Agent] Failed to initialize")


def create_app():
    app = web.Application()
    app.on_startup.append(on_startup)

    app.router.add_get('/', handle_index)
    app.router.add_get('/status', handle_status)
    app.router.add_get('/tools', handle_tools)
    app.router.add_post('/execute', handle_execute)
    app.router.add_post('/switch_registry', handle_switch_registry)
    app.router.add_post('/toggle_mitigation', handle_toggle_mitigation)

    return app


if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════════╗
    ║         ASI-04 Vulnerable Agent                  ║
    ║         Port: 5050                               ║
    ║         Registry: {}
    ╚══════════════════════════════════════════════════╝
    """.format(REGISTRY_FILE))

    app = create_app()
    web.run_app(app, host='0.0.0.0', port=5050)
