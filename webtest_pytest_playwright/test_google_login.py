from playwright.sync_api import Page, expect

def test_login(page: Page):
    # 1. 打开一个简单的登录页面 (这里以 Google 的首页为例)
    page.goto("https://www.google.com")
  

    # 2. 登录 Google
    # Google 的登录流程比较复杂，涉及多个页面和元素，我们这里只演示到输入邮箱的步骤
    # 定位并点击右上角的“登录”按钮
    page.get_by_role("button", name="登录").click()
    # 等待登录页面加载  
    page.wait_for_load_state("networkidle")
    # 输入邮箱
    page.fill("#identifierId", "jcc371620@gmail.com")
    # 点击下一步
    page.click("text=下一步")





# ... 脚本逻辑 ...


    page.pause()


 #运行pytest -vs --headed --slowmo 1000 test_google_login.py
