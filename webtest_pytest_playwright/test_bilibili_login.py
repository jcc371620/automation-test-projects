from playwright.sync_api import Page, expect

def test_simple_login(page: Page):
    # 1. 打开一个简单的登录页面 (这里以 Bilibili 的首页为例，它的登录入口很明显)
    page.goto("https://www.bilibili.com")
    
    # 2. 定位“登录”标签并点击（确保当前在账号密码输入模式）
    page.click(".header-login-entry")

    # 3. 输入账号
    # #login-username 是 Bilibili 账号框的 ID
    page.get_by_placeholder("请输入账号").fill("177xxxxxxxx")
    
    # 4. 输入密码
    # #login-passwd 是密码框的 ID
    page.get_by_placeholder("请输入密码").fill("xxxxxxxxx")

    # 5. 点击登录按钮
    page.click(".btn_primary")

    # ... 脚本逻辑 ...
    print("脚本跑完啦，按下回车键才会关闭浏览器...")
    input() # 等待你在终端敲一下回车

    

    page.wait_for_timeout(3000)
    #运行pytest -vs --headed --slowmo 1000 test_bilibili_login.py