from playwright.sync_api import Page, expect

def test_simple_login(page: Page):
    # 1. 打开一个简单的登录页面 (这里以 12306 的登录页为例，它的结构很直接)
    page.goto("https://kyfw.12306.cn/otn/resources/login.html")
    
    # 2. 定位“账号登录”标签并点击（确保当前在账号密码输入模式）
    page.click("text=账号登录")
    
    # 3. 输入用户名
    # #J-userName 是 12306 账号框的 ID
    page.fill("#J-userName", "177xxxxxxxx")
    
    # 4. 输入密码
    # #J-password 是密码框的 ID
    page.fill("#J-password", "xxxxxxxx")
    
    # 5. 点击立即登录按钮
    page.click("#J-login")
    
    # 6. 验证：登录后页面应该包含“我的12306”或者你的名字
    # 我们等 3 秒看看结果
    page.wait_for_timeout(3000)
    print("当前页面标题是:", page.title())

    #运行pytest -vs --headed --slowmo 1000 test_12306_login.py