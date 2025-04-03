#!/bin/bash
# Ensure CGI scripts are executable
chmod -R +x /usr/share/nginx/html/cgi-bin
# Execute the original command (e.g., starting nginx)
exec "$@"
