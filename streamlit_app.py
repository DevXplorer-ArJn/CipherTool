import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Triple DES Cipher Tool",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu, header, footer, .stDeployButton, [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        .block-container, .main, .stApp {
            margin: 0 !important;
            padding: 0 !important;
            max-width: 100% !important;
            background: #0D1117 !important;
        }
        html, body {
            margin: 0 !important;
            padding: 0 !important;
            height: 100% !important;
            background: #0D1117 !important;
        }
        iframe {
            width: 100% !important;
            height: auto !important;
            min-height: 100vh !important;
            border: none !important;
            display: block !important;
            margin: 0 !important;
            padding: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Complete HTML with embedded CSS and JS
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Triple DES Cipher Tool</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body {
            height: 100%;
            overflow-x: hidden;
        }
        
        body {
            font-family: 'Space Grotesk', sans-serif;
            background: #0D1117;
            color: #E5E7EB;
        }
        
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        
        .toast {
            visibility: hidden;
            min-width: 250px;
            background-color: #00B8D4;
            color: white;
            text-align: center;
            border-radius: 6px;
            padding: 16px;
            position: fixed;
            z-index: 9999;
            right: 20px;
            bottom: 30px;
            font-weight: 600;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.875rem;
            transition: visibility 0s, opacity 0.5s linear;
            opacity: 0;
        }
        
        .toast.show {
            visibility: visible;
            opacity: 0.95;
        }
        
        .app-wrapper {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            background: #0D1117;
        }
        
        .container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 1rem;
            width: 100%;
        }
        
        /* Header */
        header {
            position: sticky;
            top: 0;
            z-index: 10;
            background: rgba(22, 27, 34, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid #30363D;
        }
        
        .header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 4rem;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        .logo-icon {
            color: #00B8D4;
            font-size: 2rem;
        }
        
        .logo-text {
            color: white;
            font-size: 1.25rem;
            font-weight: 700;
        }
        
        .nav {
            display: flex;
            gap: 2rem;
        }
        
        .nav-link {
            color: #8B949E;
            text-decoration: none;
            font-size: 0.875rem;
            font-weight: 500;
            padding-bottom: 0.25rem;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .nav-link:hover {
            color: #00B8D4;
        }
        
        .nav-link.active {
            color: #00B8D4;
            border-bottom: 2px solid #00B8D4;
        }
        
        /* Main */
        main {
            flex: 1;
            padding: 3rem 0;
            background: #0D1117;
        }
        
        .page-content {
            display: none;
        }
        
        .page-content.active {
            display: block;
        }
        
        /* Typography */
        .page-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .page-subtitle {
            color: #8B949E;
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .section-title {
            font-size: 1.125rem;
            font-weight: 700;
            color: white;
            margin-bottom: 1rem;
        }
        
        /* Cards */
        .card {
            background: #161B22;
            border: 1px solid #30363D;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        /* Form Elements */
        label {
            display: block;
            color: white;
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        
        input, textarea {
            width: 100%;
            padding: 0.75rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid #30363D;
            border-radius: 0.5rem;
            color: #E5E7EB;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.875rem;
        }
        
        input.with-icon, textarea.with-icon {
            padding-right: 3.5rem;
        }
        
        input::placeholder, textarea::placeholder {
            color: #6B7280;
        }
        
        input:focus, textarea:focus {
            outline: none;
            border-color: #00B8D4;
            box-shadow: 0 0 0 2px rgba(0, 184, 212, 0.2);
        }
        
        /* Buttons */
        .btn {
            width: 100%;
            padding: 0.75rem 1.5rem;
            background: #00B8D4;
            color: white;
            border: none;
            border-radius: 0.5rem;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 600;
            font-size: 0.875rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transition: all 0.2s;
        }
        
        .btn:hover {
            opacity: 0.9;
            transform: translateY(-1px);
        }
        
        .btn-secondary {
            background: rgba(0, 184, 212, 0.2);
            color: #00B8D4;
        }
        
        /* Radio Options */
        .radio-group {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }
        
        .radio-option {
            flex: 1;
            min-width: 250px;
            padding: 1rem;
            background: #161B22;
            border: 1px solid #30363D;
            border-radius: 0.5rem;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .radio-option:hover {
            border-color: #00B8D4;
        }
        
        .radio-option.selected {
            border-color: #00B8D4;
            box-shadow: 0 0 0 2px rgba(0, 184, 212, 0.2);
        }
        
        .radio-title {
            font-weight: 600;
            color: white;
            margin-bottom: 0.25rem;
        }
        
        .radio-desc {
            font-size: 0.875rem;
            color: #8B949E;
        }
        
        /* Boxes */
        .warning-box {
            background: rgba(234, 179, 8, 0.1);
            border-left: 4px solid #EAB308;
            padding: 1rem;
            border-radius: 0.5rem;
            display: flex;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }
        
        .warning-text {
            color: #EAB308;
            font-size: 0.875rem;
        }
        
        .info-box {
            background: #161B22;
            border: 1px solid #30363D;
            border-radius: 0.75rem;
            padding: 1.5rem;
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .info-icon {
            color: #00B8D4;
            font-size: 2rem;
        }
        
        .info-title {
            font-size: 1.125rem;
            font-weight: 700;
            color: white;
            margin-bottom: 0.5rem;
        }
        
        .info-text {
            color: #8B949E;
            font-size: 0.875rem;
        }
        
        .success-box {
            background: rgba(34, 197, 94, 0.1);
            border-left: 4px solid #22C55E;
            padding: 1rem;
            border-radius: 0.5rem;
            color: #22C55E;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem 0;
        }
        
        .error-box {
            background: rgba(239, 68, 68, 0.1);
            border-left: 4px solid #EF4444;
            padding: 1rem;
            border-radius: 0.5rem;
            color: #EF4444;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem 0;
        }
        
        /* Utilities */
        .relative { position: relative; }
        .absolute { position: absolute; }
        .max-w-xl { max-width: 36rem; margin: 0 auto; }
        .max-w-3xl { max-width: 48rem; margin: 0 auto; }
        .mt-4 { margin-top: 1rem; }
        .mt-6 { margin-top: 1.5rem; }
        .mb-6 { margin-bottom: 1.5rem; }
        .text-center { text-align: center; }
        
        .icon-button {
            position: absolute;
            top: 50%;
            right: 0.5rem;
            transform: translateY(-50%);
            background: rgba(0, 184, 212, 0.1);
            border: 1px solid rgba(0, 184, 212, 0.3);
            border-radius: 0.375rem;
            color: #00B8D4;
            cursor: pointer;
            padding: 0.5rem;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .icon-button:hover {
            background: rgba(0, 184, 212, 0.2);
            border-color: #00B8D4;
        }
        
        .flex-buttons {
            display: flex;
            gap: 0.75rem;
        }
        
        .flex-buttons .btn {
            width: 50%;
        }
        
        /* Footer */
        footer {
            border-top: 1px solid #30363D;
            background: #161B22;
            padding: 1.5rem 0;
            text-align: center;
            color: #8B949E;
            font-size: 0.875rem;
        }
        
        .hidden {
            display: none !important;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .nav {
                gap: 1rem;
            }
            .page-title {
                font-size: 2rem;
            }
            .radio-option {
                min-width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="app-wrapper">
        <!-- Header -->
        <header>
            <div class="container">
                <div class="header-content">
                    <div class="logo">
                        <span class="material-symbols-outlined logo-icon">shield_lock</span>
                        <span class="logo-text">CipherTool</span>
                    </div>
                    <nav class="nav">
                        <a class="nav-link active" data-page="key" onclick="showPage('key')">Generate Key</a>
                        <a class="nav-link" data-page="encrypt" onclick="showPage('encrypt')">Encrypt</a>
                        <a class="nav-link" data-page="decrypt" onclick="showPage('decrypt')">Decrypt</a>
                    </nav>
                </div>
            </div>
        </header>

        <!-- Main Content -->
        <main class="container">
            <!-- Key Generation Page -->
            <div id="page-key" class="page-content active">
                <div class="max-w-3xl">
                    <h1 class="page-title">Generate Encryption Key</h1>
                    <p class="page-subtitle">Create a secure Triple DES key for your encryption needs.</p>
                    
                    <div class="card">
                        <h2 class="section-title">1. Select Key Size</h2>
                        <div class="radio-group">
                            <div class="radio-option" onclick="selectKeySize(16)">
                                <div class="radio-title">16-byte Key (128-bit)</div>
                                <div class="radio-desc">Standard security, suitable for most applications.</div>
                            </div>
                            <div class="radio-option selected" onclick="selectKeySize(24)">
                                <div class="radio-title">24-byte Key (192-bit)</div>
                                <div class="radio-desc">Enhanced security for highly sensitive data.</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <h2 class="section-title">2. Generate Your Key</h2>
                        <button class="btn" onclick="generateKey()">
                            <span class="material-symbols-outlined">autorenew</span>
                            <span>Generate New Key</span>
                        </button>
                        <div class="mt-6">
                            <label>Your Generated Key:</label>
                            <div class="relative">
                                <input id="generated-key" type="text" class="with-icon" readonly placeholder="Click 'Generate New Key' to create a key">
                                <button class="icon-button" onclick="copyKey()" title="Copy key">
                                    <span class="material-symbols-outlined">content_copy</span>
                                </button>
                            </div>
                        </div>
                        <div class="mt-4 hidden" id="download-section">
                            <button class="btn btn-secondary" onclick="downloadKey()">
                                <span class="material-symbols-outlined">download</span>
                                <span>Download Key File</span>
                            </button>
                        </div>
                    </div>
                    
                    <div class="warning-box">
                        <span class="material-symbols-outlined" style="color: #EAB308;">warning</span>
                        <div class="warning-text">
                            <strong>Important:</strong> Keep this key safe and do not share it. If you lose your key, you will permanently lose access to your encrypted data.
                        </div>
                    </div>
                    
                    <div class="info-box">
                        <span class="material-symbols-outlined info-icon">psychology</span>
                        <div>
                            <div class="info-title">How Key Generation Works</div>
                            <div class="info-text">
                                Our system uses a cryptographically secure pseudo-random number generator (CSPRNG) 
                                to create keys with high entropy. This ensures that the keys are unpredictable and 
                                resistant to brute-force attacks, forming the foundation of your data's security.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Encrypt Page -->
            <div id="page-encrypt" class="page-content">
                <div class="max-w-xl">
                    <h1 class="page-title">Encrypt Your Message</h1>
                    <p class="page-subtitle">Secure your text using the Triple DES algorithm.</p>
                    
                    <div class="card">
                        <div class="mb-6">
                            <label>Message</label>
                            <textarea id="encrypt-message" rows="4" placeholder="Enter the message to encrypt"></textarea>
                        </div>
                        
                        <div class="mb-6">
                            <label>Password / Key</label>
                            <div class="relative">
                                <input id="encrypt-password" type="password" class="with-icon" placeholder="Enter your secret key">
                                <button class="icon-button" onclick="togglePassword('encrypt-password')">
                                    <span class="material-symbols-outlined">visibility</span>
                                </button>
                            </div>
                        </div>
                        
                        <div class="text-center mb-6">
                            <span class="material-symbols-outlined" style="font-size: 2rem; color: #8B949E;">arrow_downward</span>
                        </div>
                        
                        <button class="btn" onclick="encryptMessage()">
                            <span class="material-symbols-outlined">lock</span>
                            <span>Encrypt Message</span>
                        </button>
                        
                        <div id="encrypt-result" class="mt-6 hidden">
                            <div class="success-box">
                                <span class="material-symbols-outlined">check_circle</span>
                                <span>Success</span>
                            </div>
                            <div class="relative">
                                <textarea id="encrypted-output" class="with-icon" rows="4" readonly style="font-family: monospace;"></textarea>
                                <button class="icon-button" onclick="copyText('encrypted-output')" style="top: 1rem;">
                                    <span class="material-symbols-outlined">content_copy</span>
                                </button>
                            </div>
                            <p style="color: #8B949E; font-size: 0.875rem; margin-top: 0.5rem;">Your message has been successfully encrypted.</p>
                            <div class="flex-buttons mt-4">
                                <button class="btn btn-secondary" onclick="downloadEncrypted()">
                                    <span class="material-symbols-outlined">download</span>
                                    <span>Download</span>
                                </button>
                                <button class="btn btn-secondary">
                                    <span class="material-symbols-outlined">share</span>
                                    <span>Share</span>
                                </button>
                            </div>
                        </div>
                        
                        <div id="encrypt-error"></div>
                    </div>
                </div>
            </div>

            <!-- Decrypt Page -->
            <div id="page-decrypt" class="page-content">
                <div class="max-w-xl">
                    <h1 class="page-title">Decrypt Message</h1>
                    <p class="page-subtitle">Enter your encrypted message and the password to reveal the original text.</p>
                    
                    <div class="card">
                        <div class="mb-6">
                            <label>Encrypted Message</label>
                            <textarea id="decrypt-message" rows="4" placeholder="Enter encrypted message"></textarea>
                        </div>
                        
                        <div class="mb-6">
                            <label>Password / Key</label>
                            <div class="relative">
                                <input id="decrypt-password" type="password" class="with-icon" placeholder="Enter your password">
                                <button class="icon-button" onclick="togglePassword('decrypt-password')">
                                    <span class="material-symbols-outlined">visibility</span>
                                </button>
                            </div>
                        </div>
                        
                        <div class="text-center mb-6">
                            <span class="material-symbols-outlined" style="font-size: 2rem; color: #00B8D4; transform: rotate(-90deg); display: inline-block;">arrow_right_alt</span>
                        </div>
                        
                        <button class="btn" onclick="decryptMessage()">
                            <span class="material-symbols-outlined">lock_open</span>
                            <span>Decrypt Message</span>
                        </button>
                        
                        <div id="decrypt-result" class="mt-6 hidden">
                            <div class="success-box">
                                <span class="material-symbols-outlined">check_circle</span>
                                <span>Success</span>
                            </div>
                            <div id="decrypted-output" style="background: rgba(255, 255, 255, 0.05); padding: 1rem; border-radius: 0.5rem; min-height: 6rem; color: white;"></div>
                        </div>
                        
                        <div id="decrypt-error"></div>
                    </div>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer>
            <div class="container">
                <p>© 2025 CipherTool. All Rights Reserved.</p>
            </div>
        </footer>
    </div>

    <div id="toast" class="toast"></div>

    <script>
        let selectedKeySize = 24;
        let generatedKey = '';
        
        function showToast(message) {
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.classList.add('show');
            
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }
        
        function showPage(pageName) {
            document.querySelectorAll('.page-content').forEach(page => {
                page.classList.remove('active');
            });
            
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });
            
            document.getElementById('page-' + pageName).classList.add('active');
            document.querySelector('[data-page="' + pageName + '"]').classList.add('active');
        }
        
        function selectKeySize(size) {
            selectedKeySize = size;
            document.querySelectorAll('.radio-option').forEach(opt => {
                opt.classList.remove('selected');
            });
            event.currentTarget.classList.add('selected');
        }
        
        function generateKey() {
            const array = new Uint8Array(selectedKeySize);
            window.crypto.getRandomValues(array);
            generatedKey = btoa(String.fromCharCode.apply(null, array));
            document.getElementById('generated-key').value = generatedKey;
            document.getElementById('download-section').classList.remove('hidden');
        }
        
        function copyKey() {
            const keyInput = document.getElementById('generated-key');
            if (keyInput.value) {
                keyInput.select();
                document.execCommand('copy');
                showToast('Key copied to clipboard!');
            } else {
                showToast('Please generate a key first!');
            }
        }
        
        function downloadKey() {
            if (!generatedKey) return;
            const blob = new Blob([generatedKey], { type: 'text/plain' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'triple_des_key.txt';
            a.click();
            window.URL.revokeObjectURL(url);
        }
        
        function togglePassword(id) {
            const input = document.getElementById(id);
            const icon = event.currentTarget.querySelector('.material-symbols-outlined');
            if (input.type === 'password') {
                input.type = 'text';
                icon.textContent = 'visibility_off';
            } else {
                input.type = 'password';
                icon.textContent = 'visibility';
            }
        }
        
        function encryptMessage() {
            const message = document.getElementById('encrypt-message').value;
            const password = document.getElementById('encrypt-password').value;
            
            if (!message || !password) {
                showError('encrypt-error', 'Please enter both message and password');
                return;
            }
            
            try {
                const encrypted = CryptoJS.TripleDES.encrypt(message, password).toString();
                document.getElementById('encrypted-output').value = encrypted;
                document.getElementById('encrypt-result').classList.remove('hidden');
                document.getElementById('encrypt-error').innerHTML = '';
            } catch (e) {
                showError('encrypt-error', 'Encryption failed: ' + e.message);
            }
        }
        
        function decryptMessage() {
            const encrypted = document.getElementById('decrypt-message').value;
            const password = document.getElementById('decrypt-password').value;
            
            if (!encrypted || !password) {
                showError('decrypt-error', 'Please enter both encrypted message and password');
                return;
            }
            
            try {
                const decrypted = CryptoJS.TripleDES.decrypt(encrypted, password);
                const plaintext = decrypted.toString(CryptoJS.enc.Utf8);
                
                if (!plaintext) {
                    showError('decrypt-error', 'Decryption failed. Check your password and encrypted message.');
                    return;
                }
                
                document.getElementById('decrypted-output').textContent = plaintext;
                document.getElementById('decrypt-result').classList.remove('hidden');
                document.getElementById('decrypt-error').innerHTML = '';
            } catch (e) {
                showError('decrypt-error', 'Decryption failed: ' + e.message);
            }
        }
        
        function showError(elementId, message) {
            const errorDiv = document.getElementById(elementId);
            errorDiv.className = 'error-box';
            errorDiv.innerHTML = '<span class="material-symbols-outlined">error</span><span>' + message + '</span>';
        }
        
        function copyText(elementId) {
            const element = document.getElementById(elementId);
            element.select();
            document.execCommand('copy');
            showToast('Copied to clipboard!');
        }
        
        function downloadEncrypted() {
            const text = document.getElementById('encrypted-output').value;
            const blob = new Blob([text], { type: 'text/plain' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'encrypted_message.txt';
            a.click();
            window.URL.revokeObjectURL(url);
        }
    </script>
</body>
</html>
"""

components.html(html_code, scrolling=True,)