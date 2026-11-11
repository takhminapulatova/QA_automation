import requests

def test_get_status():
    response = requests.get('https://httpbin.org/get')
    assert response.status_code == 200
    assert response.json()["url"] == "https://httpbin.org/get"

def test_get_404():
    response = requests.get('https://httpbin.org/status/404')
    assert response.status_code == 404

def test_get_with_params():
    response = requests.get('https://httpbin.org/get', params={"name": "Ada"})
    assert response.json()["args"]["name"] == "Ada"

def test_post():
    response = requests.post('https://httpbin.org/post', json={"role": "student"})
    assert response.json()["json"]["role"] == "student"
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 5

def test_headers():
    response = requests.get('https://httpbin.org/headers')
    assert response.status_code == 200
    assert "headers" in response.json()
    assert "User-Agent" in response.json()["headers"]
