import requests

def test_get_request():
    # 1. Send a GET request to the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Validate the response status code and content
    response = requests.get(url)
    
    # 3. print the response for debugging purposes
    print(f"\n状态码: {response.status_code}")
    print(f"返回数据: {response.json()}")
    print(f"响应内容: {response.text}")
    print(f"响应头: {response.headers}")
    print(f"响应时间: {response.elapsed.total_seconds()} 秒")
    print(f"请求方法: {response.request.method}")

    # 4. Assert the response status code and content
    # Check if the status code is 200 (OK)
    assert response.status_code == 200

    #Check if the response contains the expected data
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert data["userId"] == 1

    #run pytest -vs test_api.py