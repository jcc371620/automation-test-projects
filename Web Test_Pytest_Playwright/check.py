from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 尝试启动 Chromium 浏览器
    browser = p.chromium.launch(headless=False) # headless=False 会让你看到窗口
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    print(f"页面标题是: {page.title()}")
    browser.close()
    print("恭喜！Playwright 已完美运行！")