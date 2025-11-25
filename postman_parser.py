import json

def parse_postman_collection(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    requests = []
    for item in data.get("item", []):
        req = item.get("request", {})
        requests.append({
            "name": item.get("name"),
            "method": req.get("method"),
            "url": req.get("url", {}).get("raw"),
            "headers": {h["key"]: h["value"] for h in req.get("header", [])},
            "body": req.get("body", {}).get("raw")
        })
    return requests