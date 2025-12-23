#!/bin/bash

# Use Python to process JSON and write CSV
python3 - <<EOF
import json
import csv

input_path = '/app/input.json'
output_path = '/app/output.csv'

try:
    with open(input_path, 'r') as f:
        data = json.load(f)

    active_users = [
        {'name': user['name'], 'email': user['email']} 
        for user in data if user.get('active') is True
    ]

    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'email'])
        writer.writeheader()
        writer.writerows(active_users)
    
    print(f"Successfully processed {len(active_users)} active users.")
except Exception as e:
    print(f"Error: {e}")
    exit(1)
EOF
