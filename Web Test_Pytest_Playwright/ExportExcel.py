from playwright.sync_api import sync_playwright
from playwright_stealth import stealth
import pandas as pd  # 导入 pandas

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # 【关键】启动“潜行模式”，隐藏自动化特征
        stealth(page)

        print("🔍 正在搜索...")
        page.goto("https://www.google.com")
        
        # 搜索
        search_box = page.locator("textarea[name='q']")
        search_box.fill("Playwright")
        search_box.press("Enter")
        
        # 等待结果加载
        page.wait_for_selector("h3")
        
        # --- 核心逻辑：提取数据 ---
        data_list = []
        
        # 找到所有的搜索结果块
        # Google 的结果通常在 id 为 search 的 div 里的 g 类中
        results = page.locator("#search .g").all()
        
        print(f"找到 {len(results)} 条结果，正在抓取前 5 条...")
        
        for res in results[:5]:
            try:
                # 抓取标题 (h3 标签)
                title = res.locator("h3").inner_text()
                # 抓取链接 (a 标签的 href 属性)
                link = res.locator("a").first.get_attribute("href")
                
                # 把这一行数据存进字典
                data_list.append({
                    "标题": title,
                    "链接": link
                })
            except:
                continue # 如果某一条抓取失败，跳过它
        
        # --- 核心逻辑：保存为 Excel ---
        if data_list:
            # 1. 把列表转换成 pandas 的 DataFrame (类似表格的对象)
            df = pd.DataFrame(data_list)
            
            # 2. 保存到 Excel 文件
            file_name = "google_results.xlsx"
            df.to_excel(file_name, index=False)
            
            print(f"✨ 成功！数据已保存到: {file_name}")
        else:
            print("❌ 未抓取到数据")

        browser.close()

if __name__ == "__main__":
    run()