import requests

def test_post_request():
    # 1. Send a POST request to the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Pytest learning",
        "body": "Post learning with pytest and requests",
        "userId": 1
    }

    # 2. Validate the response status code and content
    response = requests.post(url, json=payload)
    
    # 3. print the response for debugging purposes
    print(f"\n状态码: {response.status_code}")
    print(f"返回数据: {response.json()}")
    print(f"响应内容: {response.text}")
    print(f"响应头: {response.headers}")
    print(f"响应时间: {response.elapsed.total_seconds()} 秒")
    print(f"请求方法: {response.request.method}")

    # 4. Assert the response status code and content
    # Check if the status code is 201 (Created)
    assert response.status_code == 201

    #Check if the response contains the expected data
    data = response.json()
    assert data["title"] == "Pytest learning"
    assert data["body"] == "Post learning with pytest and requests"
    assert data["userId"] == 1