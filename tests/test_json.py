import json

response = '{"username": "tomsmith", "age": 30, "active": true}'
data = json.loads(response)

def test_user_json():
    assert data['username'] == "tomsmith"
    assert data['active'] is True
    assert data['age'] == 30
    assert "email" not in data
