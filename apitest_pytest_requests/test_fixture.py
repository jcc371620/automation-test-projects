import pytest
import requests

# 这个 fixture 会先运行，并把拿到的 token 传给下面的函数
@pytest.fixture
def auth_token():
    url = "https://example.com/api/login"
    res = requests.post(url, json={"u": "admin", "p": "123"})
    return res.json()["token"]

# 这个测试函数直接“点菜”使用 auth_token
def test_get_order_list(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    r = requests.get("https://example.com/api/orders", headers=headers)
    assert r.status_code == 200

def test_get_settings(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    r = requests.get("https://example.com/api/settings", headers=headers)
    assert r.status_code == 200