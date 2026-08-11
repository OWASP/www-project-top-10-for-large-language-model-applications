"""
ASI-04 Lab - Legitimate MCP Server
Safe document helper tool server
Port: 5001
"""

import json
import logging
from aiohttp import web

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LegitMCPServer:
    """Legitimate document helper MCP server"""

    def __init__(self):
        self.tools = self._register_tools()

    def _register_tools(self):
        """Register legitimate tools"""
        return {
            "search_documents": {
                "name": "search_documents",
                "description": "Search internal documents and knowledge base for relevant information.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query"
                        }
                    },
                    "required": ["query"]
                }
            },
            "get_document": {
                "name": "get_document",
                "description": "Retrieve a specific document by ID or path.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "doc_id": {
                            "type": "string",
                            "description": "Document identifier"
                        }
                    },
                    "required": ["doc_id"]
                }
            }
        }

    async def handle_search_documents(self, params: dict) -> dict:
        """Handle legitimate document search"""
        query = params.get("query", "")
        logger.info(f"[LEGIT] Searching for: {query}")

        return {
            "results": [
                {
                    "title": "Company Handbook",
                    "snippet": f"Results for '{query}': Found in section 3.2...",
                    "source": "handbook.pdf",
                    "score": 0.95
                },
                {
                    "title": "Project Documentation",
                    "snippet": f"Relevant content for '{query}' found in documentation",
                    "source": "docs/project.md",
                    "score": 0.87
                }
            ],
            "total": 2,
            "query": query
        }

    async def handle_get_document(self, params: dict) -> dict:
        """Handle legitimate document retrieval"""
        doc_id = params.get("doc_id", "")
        logger.info(f"[LEGIT] Retrieving document: {doc_id}")

        return {
            "document": {
                "id": doc_id,
                "title": f"Document {doc_id}",
                "content": f"This is the content of document {doc_id}. All data stays secure.",
                "metadata": {
                    "author": "System",
                    "created": "2024-01-01"
                }
            }
        }


# HTTP Handlers
mcp_server = LegitMCPServer()

async def handle_list_tools(request):
    """MCP list_tools endpoint"""
    return web.json_response({
        "tools": list(mcp_server.tools.values())
    })

async def handle_call_tool(request):
    """MCP call_tool endpoint"""
    try:
        body = await request.json()
        tool_name = body.get("name")
        params = body.get("arguments", {})

        handlers = {
            "search_documents": mcp_server.handle_search_documents,
            "get_document": mcp_server.handle_get_document
        }

        if tool_name in handlers:
            result = await handlers[tool_name](params)
            return web.json_response({
                "content": [{"type": "text", "text": json.dumps(result)}]
            })
        else:
            return web.json_response({
                "error": f"Unknown tool: {tool_name}"
            }, status=404)

    except Exception as e:
        logger.error(f"Error handling tool call: {e}")
        return web.json_response({
            "error": str(e)
        }, status=500)

async def handle_health(request):
    """Health check endpoint"""
    return web.json_response({
        "status": "healthy",
        "server": "document-helper",
        "port": 5001,
        "type": "legitimate"
    })

async def handle_manifest(request):
    """Server manifest/info endpoint"""
    return web.json_response({
        "name": "document-helper",
        "version": "1.0.0",
        "description": "Legitimate document search and retrieval service",
        "author": "Internal IT",
        "tools": list(mcp_server.tools.keys()),
        "endpoint": "http://localhost:5001"
    })

def create_app():
    app = web.Application()
    app.router.add_get('/health', handle_health)
    app.router.add_get('/manifest', handle_manifest)
    app.router.add_post('/mcp/list_tools', handle_list_tools)
    app.router.add_post('/mcp/call_tool', handle_call_tool)
    app.router.add_get('/tools', handle_list_tools)
    app.router.add_post('/tools/call', handle_call_tool)

    return app

if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════════╗
    ║   LEGITIMATE MCP SERVER: document-helper         ║
    ║   Port: 5001                                     ║
    ║   Status: Safe & Secure                          ║
    ╚══════════════════════════════════════════════════╝
    """)

    app = create_app()
    web.run_app(app, host='0.0.0.0', port=5001)
