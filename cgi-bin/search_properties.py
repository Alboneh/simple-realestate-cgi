#!/usr/bin/env python3
import cgi
import json

print("Content-Type: application/json\n")

# For demonstration, we use a hardcoded list of properties
properties = [
    {"id": 1, "name": "Luxury Apartment", "price": 500000, "location": "Tokyo"},
    {"id": 2, "name": "Beach House", "price": 1200000, "location": "Osaka"},
    {"id": 3, "name": "Urban Condo", "price": 750000, "location": "Yokohama"}
]

# Get query parameter 'q' (search term)
form = cgi.FieldStorage()
query = form.getvalue('q', '').lower()

# Filter properties by name or location matching the query
result = [prop for prop in properties if query in prop['name'].lower() or query in prop['location'].lower()]

print(json.dumps(result))
