import pytest
import requests

# 这个 fixture 会先运行，并把拿到的 token 传给下面的函数
# 这样就实现了“先登录拿 token，再用 token 去访问其他接口”的流程
# 这个设计非常适合需要先认证才能访问的 API 测试场景
# 通过 fixture，我们把“获取 token”的逻辑抽象出来，测试函数只关注“用 token 做什么”，提高了代码的复用性和可读性。
# 当然，如果 token 获取失败，pytest 会直接报错，后续的测试函数就不会执行，这也是 pytest 的一个优点，可以避免无意义的测试执行。
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

# fixture用来“准备测试环境 + 提供测试数据 + 做清理工作”
# example 1
def test_a():
    db = connect_db()
    # ...

def test_b():
    db = connect_db()
    # ...

import pytest
@pytest.fixture
def db():
    return connect_db()

def test_a(db):
    ...

def test_b(db):
    ...

#   example 1 提供测试数据（最基础）
import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "age": 20}

def test_user_name(user):
    assert user["name"] == "Alice"
    提供测试用的数据
    多个测试共享

#   例子2：初始化资源（比如数据库/客户端）
import pytest

@pytest.fixture
def db_connection():
    print("连接数据库")
    conn = "db_conn"
    yield conn
    print("关闭数据库")
def test_query(db_connection):
    assert db_connection == "db_conn"

关键点：
yield 前：初始化
yield 后：清理资源

#例子3：接口测试（很接近真实项目）
接口测试（很接近真实项目）
import pytest
import requests

@pytest.fixture
def api_client():
    return requests.Session()

def test_get_user(api_client):
    res = api_client.get("https://api.example.com/user")
    assert res.status_code == 200

作用：
统一管理 HTTP client
避免每个测试都 new 一次