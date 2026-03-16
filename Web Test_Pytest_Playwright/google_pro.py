from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # 启动浏览器，慢动作设为 800 毫秒，方便你看清
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()
        
        print("🌍 正在前往 Google...")
        page.goto("https://www.google.com")
        
        # 1. 定位搜索框
        # Google 的搜索框通常有 name="q"，我们直接通过这个属性找它
        search_box = page.locator("textarea[name='q']")
        
        print("⌨️ 正在输入关键词...")
        search_box.fill("Playwright Python tutorial")
        search_box.press("Enter")
        
        # 2. 等待结果加载
        # Google 搜索结果的标题通常都在 <h3> 标签里
        page.wait_for_selector("h3")
        
        # 3. 打印出前三个结果的标题，让你看看它搜到了什么
        results = page.locator("h3").all()
        print("\n--- 搜索结果前三名 ---")
        for i, res in enumerate(results[:3]):
            print(f"{i+1}. {res.inner_text()}")
        
        # 4. 【高能动作】点击第一个搜索结果
        print("\n🖱️ 正在点击第一个结果...")
        results[0].click()
        
        # 5. 等待 3 秒，让你看看跳进去的网页
        page.wait_for_timeout(3000)
        
        print(f"✅ 最终页面标题: {page.title()}")
        browser.close()

if __name__ == "__main__":
    run()