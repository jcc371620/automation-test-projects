from playwright.sync_api import sync_playwright
import page

def run():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        print("正在前往 Google...")
        try:
            # 1. 访问 Google
            page.goto("https://www.google.com", timeout=10000)
            
            # 2. 定位搜索框
            # Google 的搜索框很特别，用 name="q" 定位是最稳的
            search_box = page.get_by_role("combobox", name="搜索") 
            # 如果上面那行不行，可以用通用定位：page.locator("textarea[name='q']")
            
            print("正在输入关键词...")
            search_box.fill("Playwright automation")
            
            # 3. 敲回车
            print("按回车键...")
            search_box.press("Enter")
            
            # 4. 关键：等搜索结果出来
            # 我们等 Google 的“工具”按钮出现，这代表结果页加载完了
            page.wait_for_load_state("networkidle")
            
            print(f"当前页面标题是: {page.title()}")
            page.screenshot(path="google_result.png")
            print("截图已保存！")
            
        except Exception as e:
            print(f"出错了：{e}")
            # 如果是因为连不上 Google，这里会报错
            
        finally:
            page.wait_for_timeout(3000)
            browser.close()

if __name__ == "__main__":
    run()