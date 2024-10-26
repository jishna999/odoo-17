import requests
import json

url = 'http://localhost:8077/jsonrpc'
headers = {'Content-Type': 'application/json'}

create_payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "model": "res.partner",
        "method": "create",
        "args": [{
            "name": "New Partner",
            "is_company": True
        }],
        "kwargs": {}
    },
    "id": 1
}

response = requests.post(url, headers=headers, data=json.dumps(create_payload))

if response.status_code == 200:
    data = response.json()
    print("Create Result:", json.dumps(data, indent=4))
else:
    print("Create Error:", response.status_code, response.text)

