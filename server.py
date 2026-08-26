import http.server
import socketserver
import socket

PORT = 8000
# Get your local IP address for the network link
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Local address: http://localhost:{PORT}")
    print(f"Network address: http://{local_ip}:{PORT}")
    print("Press Ctrl+C to stop.")
    httpd.serve_forever()

