"""
ASI04 Lab - Attacker Collection Server
Receives and logs all exfiltrated data from supply chain attacks
"""

from flask import Flask, request, jsonify
from datetime import datetime
import json
import os
import hashlib

app = Flask(__name__)

# Store collected data
COLLECTED_DIR = "/app/collected"
os.makedirs(COLLECTED_DIR, exist_ok=True)

# In-memory log for dashboard
exfil_log = []

def load_collected_files():
    """Load existing collected files into memory on startup"""
    global exfil_log
    exfil_log = []

    if not os.path.exists(COLLECTED_DIR):
        return

    files = sorted([f for f in os.listdir(COLLECTED_DIR) if f.endswith('.json')])

    for filename in files:
        try:
            with open(os.path.join(COLLECTED_DIR, filename), 'r') as f:
                entry = json.load(f)
                exfil_log.append(entry)
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    print(f"Loaded {len(exfil_log)} existing entries from disk")

# Load existing data on startup
load_collected_files()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "collected_count": len(exfil_log)})

@app.route('/collect', methods=['POST', 'GET'])
def collect():
    """Main exfiltration endpoint"""
    timestamp = datetime.utcnow().isoformat()
    
    # Handle both GET (query params) and POST (JSON body)
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
        except:
            data = {"raw": request.data.decode('utf-8', errors='ignore')}
    else:
        data = dict(request.args)
        # Handle base64 encoded data in 'd' parameter
        if 'd' in data:
            import base64
            try:
                decoded = base64.b64decode(data['d']).decode('utf-8')
                data['decoded'] = decoded
            except:
                pass
    
    # Extract source info
    source_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'unknown')
    
    entry = {
        "id": hashlib.md5(f"{timestamp}{source_ip}".encode()).hexdigest()[:8],
        "timestamp": timestamp,
        "source_ip": source_ip,
        "user_agent": user_agent,
        "attack_type": data.get("type", "unknown"),
        "data": data
    }
    
    exfil_log.append(entry)
    
    # Save to file
    filename = f"{COLLECTED_DIR}/{entry['id']}_{timestamp.replace(':', '-')}.json"
    with open(filename, 'w') as f:
        json.dump(entry, f, indent=2)
    
    # Log to console for visibility
    print(f"\n{'='*60}")
    print(f"[EXFIL RECEIVED] {timestamp}")
    print(f"Type: {entry['attack_type']}")
    print(f"Source: {source_ip}")
    print(f"Data: {json.dumps(data, indent=2)[:500]}")
    print(f"{'='*60}\n")
    
    return jsonify({"status": "received", "id": entry['id']})

@app.route('/collect/credentials', methods=['POST'])
def collect_credentials():
    """Specific endpoint for credential exfiltration"""
    data = request.get_json(force=True)
    data['type'] = 'credentials'
    
    # Check for flags
    flags_found = []
    data_str = json.dumps(data)
    
    flag_patterns = [
        "ASI04_FLAG",
        "sk-live-",
        "AKIA",
        "password",
        "secret"
    ]
    
    for pattern in flag_patterns:
        if pattern.lower() in data_str.lower():
            flags_found.append(pattern)
    
    if flags_found:
        print(f"\n🚨 POTENTIAL FLAG/SECRET CAPTURED: {flags_found}")
    
    return collect()

@app.route('/collect/file', methods=['POST'])
def collect_file():
    """Endpoint for file content exfiltration"""
    data = request.get_json(force=True)
    data['type'] = 'file_exfil'
    return collect()

@app.route('/collect/query', methods=['POST'])
def collect_query():
    """Endpoint for search query exfiltration"""
    data = request.get_json(force=True)
    data['type'] = 'search_query'
    return collect()

@app.route('/collect/rag', methods=['POST'])
def collect_rag():
    """Endpoint for RAG retrieval exfiltration"""
    data = request.get_json(force=True)
    data['type'] = 'rag_retrieval'
    return collect()

@app.route('/dashboard', methods=['GET'])
def dashboard():
    """Simple HTML dashboard to view collected data"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ASI04 Attacker Dashboard</title>
        <style>
            body { font-family: monospace; background: #1a1a2e; color: #00ff00; padding: 20px; }
            h1 { color: #ff0000; }
            .entry { background: #16213e; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #00ff00; }
            .timestamp { color: #888; }
            .type { color: #ff6b6b; font-weight: bold; }
            .data { background: #0f0f23; padding: 10px; margin-top: 10px; overflow-x: auto; }
            pre { margin: 0; white-space: pre-wrap; }
            .flag { background: #ff0; color: #000; padding: 2px 5px; }
        </style>
        <script>
            setTimeout(() => location.reload(), 5000);
        </script>
    </head>
    <body>
        <h1>🎯 ASI04 Attacker Collection Server</h1>
        <p>Total captured: <strong>%d</strong> entries</p>
        <p><em>Auto-refreshes every 5 seconds</em></p>
        <hr>
        %s
    </body>
    </html>
    """
    
    entries_html = ""
    for entry in reversed(exfil_log[-50:]):  # Last 50 entries
        data_str = json.dumps(entry['data'], indent=2)
        
        # Highlight flags
        for flag in ["ASI04_FLAG", "sk-live", "AKIA", "password", "secret"]:
            if flag.lower() in data_str.lower():
                data_str = data_str.replace(flag, f'<span class="flag">{flag}</span>')
        
        entries_html += f"""
        <div class="entry">
            <span class="timestamp">{entry['timestamp']}</span> | 
            <span class="type">{entry['attack_type']}</span> |
            ID: {entry['id']}
            <div class="data"><pre>{data_str}</pre></div>
        </div>
        """
    
    return html % (len(exfil_log), entries_html or "<p>No data collected yet. Start exploiting!</p>")

@app.route('/api/log', methods=['GET'])
def api_log():
    """API endpoint for CTF dashboard"""
    return jsonify({
        "count": len(exfil_log),
        "entries": exfil_log[-100:]
    })

@app.route('/api/flags', methods=['GET'])
def api_flags():
    """Check which flags have been captured"""
    all_data = json.dumps(exfil_log)
    
    flags = {
        "ASI04_01_typosquat": "ASI04_FLAG{typ0squ4t_g0t_y0u}" in all_data,
        "ASI04_02_mcp": "ASI04_FLAG{mcp_tr0j4n_d3t3ct3d}" in all_data or "SECRET_API_KEY" in all_data,
        "ASI04_03_depconfusion": "ASI04_FLAG{d3p_c0nfus10n_pwn3d}" in all_data,
        "ASI04_04_toolpoison": "ASI04_FLAG{h1dd3n_1nstruct10ns}" in all_data,
        "ASI04_05_rag": "ASI04_FLAG{r4g_p01s0n3d}" in all_data,
    }
    
    return jsonify(flags)

@app.route('/reset', methods=['POST'])
def reset():
    """Reset collected data"""
    global exfil_log
    exfil_log = []
    
    # Clear files
    import shutil
    shutil.rmtree(COLLECTED_DIR, ignore_errors=True)
    os.makedirs(COLLECTED_DIR, exist_ok=True)
    
    return jsonify({"status": "reset complete"})

if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║         ASI04 ATTACKER COLLECTION SERVER                     ║
    ║         Ready to receive exfiltrated data                    ║
    ║         Dashboard: http://localhost:8666/dashboard           ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    app.run(host='0.0.0.0', port=8666, debug=True)
