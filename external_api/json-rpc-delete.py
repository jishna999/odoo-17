import requests
import json

url = 'http://localhost:8077/web/dataset/call_kw'
headers = {'Content-Type': 'application/json'}

# Define the JSON-RPC request payload for deleting a record
delete_payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "model": "res.partner",
        "method": "unlink",
        "args": [[1]],  # Replace '1' with the actual record ID you want to delete
        "kwargs": {}
    },
    "id": 1
}

response = requests.post(url, headers=headers, data=json.dumps(delete_payload))

if response.status_code == 200:
    data = response.json()
    print("Delete Result:", json.dumps(data, indent=4))
else:
    print("Error:", response.status_code, response.text)

