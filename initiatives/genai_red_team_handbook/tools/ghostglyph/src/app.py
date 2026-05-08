"""
GhostGlyph - ASCII Smuggling Tool for GenAI Red Teaming
A cyberpunk tool for encoding hidden payloads using Unicode tricks.
"""

from flask import Flask, Response, request, jsonify
from encoder import (
    encode_zero_width,
    decode_zero_width,
    encode_unicode_tags,
    decode_unicode_tags,
    encode_invisible_spaces,
    decode_invisible_spaces,
    detect_hidden_content,
)

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👻 GHOSTGLYPH // ASCII SMUGGLER</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-cyan: #00FFFF;
            --neon-magenta: #FF00FF;
            --neon-pink: #FF1493;
            --matrix-green: #00FF41;
            --hot-orange: #FF6B00;
            --deep-purple: #9D00FF;
            --bg-dark: #0a0a0f;
            --bg-darker: #050508;
            --grid-color: rgba(0, 255, 255, 0.03);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'JetBrains Mono', monospace;
            background: var(--bg-dark);
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }
        
        /* Animated grid background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(var(--grid-color) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: gridMove 20s linear infinite;
            pointer-events: none;
            z-index: 0;
        }
        
        @keyframes gridMove {
            0% { transform: perspective(500px) rotateX(60deg) translateY(0); }
            100% { transform: perspective(500px) rotateX(60deg) translateY(50px); }
        }
        
        /* Scanline effect */
        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(
                0deg,
                rgba(0, 0, 0, 0.15),
                rgba(0, 0, 0, 0.15) 1px,
                transparent 1px,
                transparent 2px
            );
            pointer-events: none;
            z-index: 1000;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            position: relative;
            z-index: 1;
        }
        
        /* Glitch title */
        .title {
            font-family: 'Orbitron', sans-serif;
            font-size: 3rem;
            font-weight: 900;
            text-align: center;
            margin-bottom: 0.5rem;
            position: relative;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta), var(--neon-pink));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: glitch 2s infinite;
            text-shadow: 0 0 10px var(--neon-cyan);
        }
        
        .title::before,
        .title::after {
            content: 'GHOSTGLYPH';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .title::before {
            animation: glitchTop 1s infinite;
            clip-path: polygon(0 0, 100% 0, 100% 33%, 0 33%);
        }
        
        .title::after {
            animation: glitchBottom 1.5s infinite;
            clip-path: polygon(0 67%, 100% 67%, 100% 100%, 0 100%);
        }
        
        @keyframes glitch {
            2%, 64% { transform: translate(0); }
            4%, 60% { transform: translate(-2px, 0); }
            62% { transform: translate(2px, 0); }
        }
        
        @keyframes glitchTop {
            2%, 64% { transform: translate(0); }
            4%, 60% { transform: translate(2px, -2px); }
            62% { transform: translate(-2px, 2px); }
        }
        
        @keyframes glitchBottom {
            2%, 64% { transform: translate(0); }
            4%, 60% { transform: translate(-2px, 2px); }
            62% { transform: translate(2px, -2px); }
        }
        
        .subtitle {
            text-align: center;
            color: var(--neon-magenta);
            font-size: 0.9rem;
            margin-bottom: 3rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            opacity: 0.8;
        }
        
        .panel {
            background: linear-gradient(135deg, rgba(0, 255, 255, 0.05), rgba(255, 0, 255, 0.05));
            border: 1px solid rgba(0, 255, 255, 0.2);
            border-radius: 4px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            position: relative;
            backdrop-filter: blur(10px);
        }
        
        .panel::before {
            content: '';
            position: absolute;
            top: -1px;
            left: 20px;
            right: 20px;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--neon-cyan), transparent);
        }
        
        .panel-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 0.8rem;
            color: var(--neon-cyan);
            text-transform: uppercase;
            letter-spacing: 0.2em;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .panel-title::before {
            content: '>';
            color: var(--matrix-green);
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0; }
        }
        
        label {
            display: block;
            font-size: 0.75rem;
            color: var(--neon-pink);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 0.5rem;
        }
        
        textarea {
            width: 100%;
            height: 120px;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(0, 255, 255, 0.3);
            border-radius: 4px;
            color: var(--matrix-green);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            padding: 1rem;
            resize: vertical;
            transition: all 0.3s ease;
        }
        
        textarea:focus {
            outline: none;
            border-color: var(--neon-cyan);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.3),
                        inset 0 0 20px rgba(0, 255, 255, 0.05);
        }
        
        textarea::placeholder {
            color: rgba(0, 255, 255, 0.3);
        }
        
        select {
            width: 100%;
            padding: 0.8rem 1rem;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 0, 255, 0.3);
            border-radius: 4px;
            color: var(--neon-magenta);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.3s ease;
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23FF00FF' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 1rem center;
        }
        
        select:focus {
            outline: none;
            border-color: var(--neon-magenta);
            box-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
        }
        
        select option {
            background: var(--bg-darker);
            color: var(--neon-magenta);
        }
        
        .btn-group {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        button {
            flex: 1;
            padding: 1rem 1.5rem;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .btn-encode {
            background: linear-gradient(135deg, var(--neon-cyan), var(--deep-purple));
            color: var(--bg-dark);
        }
        
        .btn-encode:hover {
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.5),
                        0 0 60px rgba(0, 255, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .btn-decode {
            background: linear-gradient(135deg, var(--neon-magenta), var(--hot-orange));
            color: var(--bg-dark);
        }
        
        .btn-decode:hover {
            box-shadow: 0 0 30px rgba(255, 0, 255, 0.5),
                        0 0 60px rgba(255, 0, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .btn-copy {
            background: transparent;
            border: 1px solid var(--matrix-green);
            color: var(--matrix-green);
            flex: 0 0 auto;
            padding: 1rem;
        }
        
        .btn-copy:hover {
            background: var(--matrix-green);
            color: var(--bg-dark);
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.5);
        }
        
        .btn-copy.copied {
            background: var(--matrix-green);
            color: var(--bg-dark);
        }
        
        .output-container {
            position: relative;
        }
        
        .output {
            width: 100%;
            min-height: 100px;
            background: rgba(0, 0, 0, 0.8);
            border: 1px solid rgba(0, 255, 65, 0.3);
            border-radius: 4px;
            padding: 1rem;
            color: var(--matrix-green);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            word-break: break-all;
            white-space: pre-wrap;
        }
        
        .output.has-content {
            animation: outputGlow 2s ease-out;
        }
        
        @keyframes outputGlow {
            0% { box-shadow: 0 0 30px rgba(0, 255, 65, 0.8); }
            100% { box-shadow: none; }
        }
        
        .stats {
            display: flex;
            gap: 2rem;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(0, 255, 255, 0.1);
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-value {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5rem;
            color: var(--neon-cyan);
            text-shadow: 0 0 10px var(--neon-cyan);
        }
        
        .stat-label {
            font-size: 0.65rem;
            color: rgba(255, 255, 255, 0.5);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        
        .toast {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: linear-gradient(135deg, var(--matrix-green), var(--neon-cyan));
            color: var(--bg-dark);
            padding: 1rem 2rem;
            border-radius: 4px;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 2000;
        }
        
        .toast.show {
            transform: translateY(0);
            opacity: 1;
        }
        
        .mode-tabs {
            display: flex;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid rgba(0, 255, 255, 0.2);
        }
        
        .mode-tab {
            padding: 1rem 2rem;
            background: transparent;
            border: none;
            color: rgba(255, 255, 255, 0.5);
            font-family: 'Orbitron', sans-serif;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            cursor: pointer;
            position: relative;
            transition: all 0.3s ease;
        }
        
        .mode-tab:hover {
            color: var(--neon-cyan);
        }
        
        .mode-tab.active {
            color: var(--neon-cyan);
        }
        
        .mode-tab.active::after {
            content: '';
            position: absolute;
            bottom: -1px;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
            box-shadow: 0 0 10px var(--neon-cyan);
        }
        
        .detect-results {
            margin-top: 1rem;
        }
        
        .detect-item {
            background: rgba(255, 0, 255, 0.1);
            border-left: 3px solid var(--neon-magenta);
            padding: 0.8rem 1rem;
            margin-bottom: 0.5rem;
            font-size: 0.8rem;
        }
        
        .detect-item.found {
            background: rgba(255, 107, 0, 0.1);
            border-color: var(--hot-orange);
        }
        
        .detect-label {
            color: var(--neon-pink);
            text-transform: uppercase;
            font-size: 0.7rem;
            letter-spacing: 0.1em;
        }
        
        .detect-value {
            color: var(--matrix-green);
            margin-top: 0.3rem;
            word-break: break-all;
        }
        
        .hidden {
            display: none;
        }
        
        /* Floating ghost decoration */
        .ghost {
            position: fixed;
            font-size: 4rem;
            opacity: 0.03;
            pointer-events: none;
            animation: float 6s ease-in-out infinite;
            z-index: 0;
        }
        
        .ghost-1 { top: 10%; left: 5%; animation-delay: 0s; }
        .ghost-2 { top: 60%; right: 5%; animation-delay: 2s; }
        .ghost-3 { bottom: 10%; left: 15%; animation-delay: 4s; }
        
        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(5deg); }
        }
        
        footer {
            text-align: center;
            padding: 2rem;
            color: rgba(255, 255, 255, 0.3);
            font-size: 0.7rem;
            letter-spacing: 0.1em;
        }
        
        footer a {
            color: var(--neon-cyan);
            text-decoration: none;
        }
        
        footer a:hover {
            text-shadow: 0 0 10px var(--neon-cyan);
        }
    </style>
</head>
<body>
    <div class="ghost ghost-1">👻</div>
    <div class="ghost ghost-2">👻</div>
    <div class="ghost ghost-3">👻</div>
    
    <div class="container">
        <h1 class="title">GHOSTGLYPH</h1>
        <p class="subtitle">// ASCII Smuggling for GenAI Red Teams //</p>
        
        <div class="mode-tabs">
            <button class="mode-tab active" data-mode="encode" onclick="switchMode('encode')">
                ⚡ Encode
            </button>
            <button class="mode-tab" data-mode="decode" onclick="switchMode('decode')">
                🔓 Decode
            </button>
            <button class="mode-tab" data-mode="detect" onclick="switchMode('detect')">
                🔍 Detect
            </button>
        </div>
        
        <!-- ENCODE MODE -->
        <div id="encode-mode">
            <div class="panel">
                <div class="panel-title">Input Payload</div>
                <label for="input-text">Text to Hide</label>
                <textarea id="input-text" placeholder="Enter your prompt injection payload here..."></textarea>
            </div>
            
            <div class="panel">
                <div class="panel-title">Encoding Configuration</div>
                <label for="encoding-type">Smuggling Method</label>
                <select id="encoding-type">
                    <option value="zero_width" selected>Zero-Width Characters (Default)</option>
                    <option value="unicode_tags">Unicode Tag Characters (U+E0000)</option>
                    <option value="invisible_spaces">Invisible Space Encoding</option>
                </select>
                <div class="btn-group">
                    <button class="btn-encode" onclick="encode()">⚡ Generate Payload</button>
                </div>
            </div>
            
            <div class="panel">
                <div class="panel-title">Encoded Output</div>
                <div class="output-container">
                    <div id="output" class="output">
                        <span style="color: rgba(255,255,255,0.3)">// Encoded payload will appear here...</span>
                    </div>
                    <div class="btn-group" style="margin-top: 1rem;">
                        <button class="btn-copy" onclick="copyOutput()">📋 Copy</button>
                    </div>
                </div>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-value" id="stat-input">0</div>
                        <div class="stat-label">Input Chars</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value" id="stat-output">0</div>
                        <div class="stat-label">Output Chars</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value" id="stat-ratio">0x</div>
                        <div class="stat-label">Expansion</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- DECODE MODE -->
        <div id="decode-mode" class="hidden">
            <div class="panel">
                <div class="panel-title">Encoded Input</div>
                <label for="decode-input">Paste Encoded Text</label>
                <textarea id="decode-input" placeholder="Paste encoded/smuggled text here to reveal hidden content..."></textarea>
            </div>
            
            <div class="panel">
                <div class="panel-title">Decoding Configuration</div>
                <label for="decoding-type">Expected Encoding</label>
                <select id="decoding-type">
                    <option value="zero_width" selected>Zero-Width Characters</option>
                    <option value="unicode_tags">Unicode Tag Characters</option>
                    <option value="invisible_spaces">Invisible Space Encoding</option>
                </select>
                <div class="btn-group">
                    <button class="btn-decode" onclick="decode()">🔓 Decode Payload</button>
                </div>
            </div>
            
            <div class="panel">
                <div class="panel-title">Decoded Output</div>
                <div id="decode-output" class="output">
                    <span style="color: rgba(255,255,255,0.3)">// Decoded content will appear here...</span>
                </div>
            </div>
        </div>
        
        <!-- DETECT MODE -->
        <div id="detect-mode" class="hidden">
            <div class="panel">
                <div class="panel-title">Suspicious Text</div>
                <label for="detect-input">Paste Text to Analyze</label>
                <textarea id="detect-input" placeholder="Paste any text to scan for hidden Unicode smuggling..."></textarea>
                <div class="btn-group">
                    <button class="btn-decode" onclick="detect()">🔍 Analyze Text</button>
                </div>
            </div>
            
            <div class="panel">
                <div class="panel-title">Detection Results</div>
                <div id="detect-results" class="detect-results">
                    <span style="color: rgba(255,255,255,0.3)">// Analysis results will appear here...</span>
                </div>
            </div>
        </div>
        
        <footer>
            OWASP GenAI Red Team Handbook // 
            <a href="https://github.com/OWASP/www-project-top-10-for-large-language-model-applications" target="_blank">GitHub</a>
        </footer>
    </div>
    
    <div id="toast" class="toast">✓ Copied to clipboard!</div>
    
    <script>
        let currentEncodedOutput = '';
        
        function switchMode(mode) {
            document.querySelectorAll('.mode-tab').forEach(tab => tab.classList.remove('active'));
            document.querySelector(`[data-mode="${mode}"]`).classList.add('active');
            
            document.getElementById('encode-mode').classList.add('hidden');
            document.getElementById('decode-mode').classList.add('hidden');
            document.getElementById('detect-mode').classList.add('hidden');
            document.getElementById(`${mode}-mode`).classList.remove('hidden');
        }
        
        async function encode() {
            const text = document.getElementById('input-text').value;
            const encodingType = document.getElementById('encoding-type').value;
            
            if (!text) {
                showToast('⚠ Enter text to encode!');
                return;
            }
            
            try {
                const response = await fetch('/encode', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text, encoding_type: encodingType })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    currentEncodedOutput = data.encoded;
                    const output = document.getElementById('output');
                    
                    // Show visual representation
                    output.innerHTML = `<span style="color: var(--neon-cyan);">[${data.encoded.length} invisible characters]</span>\\n\\n` +
                        `<span style="color: rgba(255,255,255,0.2);">Hex preview: ${data.hex_preview}...</span>`;
                    output.classList.add('has-content');
                    
                    // Update stats
                    document.getElementById('stat-input').textContent = text.length;
                    document.getElementById('stat-output').textContent = data.encoded.length;
                    document.getElementById('stat-ratio').textContent = (data.encoded.length / text.length).toFixed(1) + 'x';
                    
                    // Auto-copy for zero-width encoding
                    if (encodingType === 'zero_width') {
                        await copyToClipboard(currentEncodedOutput);
                        showToast('✓ Encoded & copied to clipboard!');
                    }
                } else {
                    showToast('⚠ Encoding failed!');
                }
            } catch (error) {
                console.error(error);
                showToast('⚠ Error connecting to server');
            }
        }
        
        async function decode() {
            const text = document.getElementById('decode-input').value;
            const decodingType = document.getElementById('decoding-type').value;
            
            if (!text) {
                showToast('⚠ Enter text to decode!');
                return;
            }
            
            try {
                const response = await fetch('/decode', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text, encoding_type: decodingType })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    const output = document.getElementById('decode-output');
                    output.textContent = data.decoded || '(No hidden content found)';
                    output.classList.add('has-content');
                } else {
                    showToast('⚠ Decoding failed!');
                }
            } catch (error) {
                console.error(error);
                showToast('⚠ Error connecting to server');
            }
        }
        
        async function detect() {
            const text = document.getElementById('detect-input').value;
            
            if (!text) {
                showToast('⚠ Enter text to analyze!');
                return;
            }
            
            try {
                const response = await fetch('/detect', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    const results = data.results;
                    let html = '';
                    
                    // Detection flags
                    html += `<div class="detect-item ${results.has_zero_width ? 'found' : ''}">
                        <div class="detect-label">Zero-Width Characters</div>
                        <div class="detect-value">${results.has_zero_width ? '⚠ DETECTED' : '✓ None found'}</div>
                    </div>`;
                    
                    html += `<div class="detect-item ${results.has_unicode_tags ? 'found' : ''}">
                        <div class="detect-label">Unicode Tag Characters</div>
                        <div class="detect-value">${results.has_unicode_tags ? '⚠ DETECTED' : '✓ None found'}</div>
                    </div>`;
                    
                    html += `<div class="detect-item ${results.has_invisible_spaces ? 'found' : ''}">
                        <div class="detect-label">Invisible Space Characters</div>
                        <div class="detect-value">${results.has_invisible_spaces ? '⚠ DETECTED' : '✓ None found'}</div>
                    </div>`;
                    
                    // Decoded content
                    if (results.zero_width_decoded) {
                        html += `<div class="detect-item found">
                            <div class="detect-label">Decoded (Zero-Width)</div>
                            <div class="detect-value">${escapeHtml(results.zero_width_decoded)}</div>
                        </div>`;
                    }
                    
                    if (results.unicode_tags_decoded) {
                        html += `<div class="detect-item found">
                            <div class="detect-label">Decoded (Unicode Tags)</div>
                            <div class="detect-value">${escapeHtml(results.unicode_tags_decoded)}</div>
                        </div>`;
                    }
                    
                    // Suspicious chars
                    if (results.suspicious_chars && results.suspicious_chars.length > 0) {
                        html += `<div class="detect-item found">
                            <div class="detect-label">Suspicious Characters Found: ${results.suspicious_chars.length}</div>
                            <div class="detect-value" style="font-size: 0.75rem; max-height: 150px; overflow-y: auto;">`;
                        
                        const shown = results.suspicious_chars.slice(0, 20);
                        shown.forEach(c => {
                            html += `${c.code} - ${c.name}<br>`;
                        });
                        
                        if (results.suspicious_chars.length > 20) {
                            html += `... and ${results.suspicious_chars.length - 20} more`;
                        }
                        
                        html += `</div></div>`;
                    }
                    
                    document.getElementById('detect-results').innerHTML = html;
                }
            } catch (error) {
                console.error(error);
                showToast('⚠ Error connecting to server');
            }
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        async function copyToClipboard(text) {
            try {
                await navigator.clipboard.writeText(text);
                return true;
            } catch (err) {
                console.error('Failed to copy:', err);
                return false;
            }
        }
        
        async function copyOutput() {
            if (currentEncodedOutput) {
                const success = await copyToClipboard(currentEncodedOutput);
                if (success) {
                    showToast('✓ Copied to clipboard!');
                    document.querySelector('.btn-copy').classList.add('copied');
                    setTimeout(() => {
                        document.querySelector('.btn-copy').classList.remove('copied');
                    }, 1000);
                }
            } else {
                showToast('⚠ Nothing to copy!');
            }
        }
        
        function showToast(message) {
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2000);
        }
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    return Response(HTML_TEMPLATE, mimetype='text/html')


@app.route('/encode', methods=['POST'])
def encode_text():
    data = request.get_json()
    text = data.get('text', '')
    encoding_type = data.get('encoding_type', 'zero_width')
    
    try:
        if encoding_type == 'zero_width':
            encoded = encode_zero_width(text)
        elif encoding_type == 'unicode_tags':
            encoded = encode_unicode_tags(text)
        elif encoding_type == 'invisible_spaces':
            encoded = encode_invisible_spaces(text)
        else:
            return jsonify({'success': False, 'error': 'Unknown encoding type'})
        
        # Generate hex preview for display
        hex_preview = ' '.join(f'{ord(c):04X}' for c in encoded[:10])
        
        return jsonify({
            'success': True,
            'encoded': encoded,
            'hex_preview': hex_preview,
            'length': len(encoded),
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/decode', methods=['POST'])
def decode_text():
    data = request.get_json()
    text = data.get('text', '')
    encoding_type = data.get('encoding_type', 'zero_width')
    
    try:
        if encoding_type == 'zero_width':
            decoded = decode_zero_width(text)
        elif encoding_type == 'unicode_tags':
            decoded = decode_unicode_tags(text)
        elif encoding_type == 'invisible_spaces':
            decoded = decode_invisible_spaces(text)
        else:
            return jsonify({'success': False, 'error': 'Unknown encoding type'})
        
        return jsonify({
            'success': True,
            'decoded': decoded,
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/detect', methods=['POST'])
def detect_text():
    data = request.get_json()
    text = data.get('text', '')
    
    try:
        results = detect_hidden_content(text)
        return jsonify({
            'success': True,
            'results': results,
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)

