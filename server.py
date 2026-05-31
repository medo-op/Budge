#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 5060
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build", "web")

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('X-Frame-Options', 'ALLOWALL')
        self.send_header('Content-Security-Policy', 'frame-ancestors *')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # Suppress logs

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    with ReusableTCPServer(('0.0.0.0', PORT), CORSHandler) as httpd:
        print(f"Serving Budget Flow on port {PORT}")
        httpd.serve_forever()
