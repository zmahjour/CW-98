import requests

requests.post(
    url="http://127.0.0.1:9999",
    json={"id": 1, "title": "study", "description": "study html and css"},
)
