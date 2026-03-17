import re
import pytest
from playwright.sync_api import Page, expect

# 这是一个测试函数，pytest 看到 test_ 开头的函数就会自动运行它
from playwright.sync_api import Page, expect

def test_baidu_search(page: Page):
    # 1. 前往百度
    page.goto("https://www.baidu.com")
    
    # 2. 定位搜索框
    search_input = page.locator("#kw")
    
    # 3. 【关键改动】先强制点击一下，确保焦点真的进去了
    # 这能解决“看得见摸不着”的问题
    search_input.click()
    
    # 4. 【关键改动】模拟真人打字，每个字间隔 100 毫秒
    # 这样不容易被百度识别成“生硬的机器人”
    search_input.type("pytest 自动化测试", delay=100)
    
    # 5. 敲回车执行搜索
    search_input.press("Enter")
    
    # 6. 等待结果，看看标题对不对
    page.wait_for_timeout(2000)
    assert "pytest" in page.title()

    print("测试通过！标题确实包含 pytest")