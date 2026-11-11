from playwright.sync_api import sync_playwright

def test_auto_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dynamic_controls")

        page.get_by_role("button", name="Enable").click()

        page.locator("#input-example input").fill("Hello Playwright!")

        browser.close()
