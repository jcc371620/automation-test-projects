import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/?zx=1773656693225&no_sw_cr=1")
    page.get_by_role("combobox", name="搜索").click()
    page.get_by_role("combobox", name="搜索").fill("playwright")
    page.locator("iframe[name=\"a-ofmdk75gjgx7\"]").content_frame.get_by_role("checkbox", name="进行人机身份验证").click()
    page.locator("iframe[name=\"c-ofmdk75gjgx7\"]").content_frame.locator("[id=\"3\"]").click()
    page.locator("iframe[name=\"c-ofmdk75gjgx7\"]").content_frame.locator("[id=\"4\"]").click()
    page.locator("iframe[name=\"c-ofmdk75gjgx7\"]").content_frame.locator("[id=\"8\"]").click()
    page.locator("iframe[name=\"c-ofmdk75gjgx7\"]").content_frame.locator("[id=\"4\"]").click()
    page.locator("iframe[name=\"c-ofmdk75gjgx7\"]").content_frame.locator("[id=\"3\"]").click()
    page.locator("iframe[name=\"c-ofmdk75gjgx7\"]").content_frame.locator("[id=\"4\"]").click()
    page.locator("iframe[name=\"c-ofmdk75gjgx7\"]").content_frame.get_by_role("button", name="验证", exact=True).click()
    page.goto("https://www.google.com/search?q=playwright&sca_esv=38c74ef179c9a07c&source=hp&ei=dtq3aZm9FZ2Qur8P9vm08AI&iflsig=AFdpzrgAAAAAabfohtzQNG9ns_Tcn5wJnS7vPZ4mXxKy&ved=0ahUKEwiZ0OGJmqSTAxUdiO4BHfY8DS4Q4dUDCA4&uact=5&oq=playwright&gs_lp=Egdnd3Mtd2l6IgpwbGF5d3JpZ2h0MgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjotQlQ2pwJWIapCXABeACQAQCYAbkCoAHHF6oBBTItOS4yuAEDyAEA-AEBmAIKoALgFagCAMICCxAuGIAEGNEDGMcBwgIFEC4YgASYA44C8QVWLBZs8mXWwZIHBTItOC4yoAfPI7IHBTItOC4yuAfgFcIHBTAuOS4xyAcbgAgA&sclient=gws-wiz&sei=kdu3aY7OBMS8kPIP-riF4A8")
    page.get_by_role("link", name="Playwright Wikipedia https://").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

 #运行pytest -vs --headed --slowmo 1000 test_codegen.py