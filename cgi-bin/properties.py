#!/usr/bin/env python3
import json

print("Content-Type: application/json\n")
properties = [
    {"id": 1, "name": "Luxury Apartment", "price": 500000},
    {"id": 2, "name": "Beach House", "price": 1200000}
]
print(json.dumps(properties))
