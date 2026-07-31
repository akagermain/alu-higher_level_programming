#!/bin/bash
# Sends a GET request to a URL and displays the body only for a 200 response.
curl -sL "$1" -w "%{http_code}" | sed '$d'
