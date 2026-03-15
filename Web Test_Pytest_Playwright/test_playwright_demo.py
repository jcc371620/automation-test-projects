import pytest
from playwright.sync_api import Page, expect

def test_baidu_search(page: Page):
    # 1. 打开网页
    page.goto("https://www.google.com")
    
    # 2. 定位搜索框并输入 (Playwright 会自动等待搜索框出现)
    # '#kw' 是百度搜索框的“身份证号”（ID）
    page.fill("#kw", "pytest 自动化测试")
    
    # 3. 按下回车键
    page.press("#kw", "Enter")
    
    # 4. 断言：验证页面上是否出现了某个结果
    # 这里我们断言页面标题里包含 "pytest"
    expect(page).to_have_title(compile("pytest"))