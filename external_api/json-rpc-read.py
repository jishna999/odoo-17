import requests
import json

url = 'http://localhost:8077/web/dataset/call_kw'
headers = {'Content-Type': 'application/json'}

# Define the JSON-RPC request payload for reading records
read_payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "model": "res.partner",
        "method": "search_read",
        "args": [[['is_company', '=', True]]],
        "kwargs": {
            "fields": ['name', 'country_id', 'comment'],
            "limit": 5
        }
    },
    "id": 1
}

response = requests.post(url, headers=headers, data=json.dumps(read_payload))

if response.status_code == 200:
    data = response.json()
    print("Read Result:", json.dumps(data, indent=4))
else:
    print("Error:", response.status_code, response.text)

