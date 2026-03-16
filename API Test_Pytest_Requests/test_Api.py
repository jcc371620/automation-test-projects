import requests

def test_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"