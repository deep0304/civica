from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    if os.path.exists('index.html'):
        return send_file('index.html')
    else:
        return "<h1>Error: index.html not found</h1><p>Make sure index.html is in the same directory as this script.</p>", 404

if __name__ == "__main__":
    print("=" * 50)
    print("Frontend Server Starting...")
    print("URL: http://localhost:8080")
    print("Make sure:")
    print("1. index.html exists in current directory")
    print("2. Proxy server is running on port 8000")
    print("=" * 50)
    
    # Check if required files exist
    if not os.path.exists('index.html'):
        print("WARNING: index.html not found!")
        
    app.run(host='127.0.0.1', port=8080, debug=True)
