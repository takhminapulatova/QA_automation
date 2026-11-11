from playwright.sync_api import sync_playwright, expect

def test_notification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        page.get_by_role("button", name="Start").click()

        expect(page.locator("#finish")).to_be_visible(timeout=10000)

        browser.close()
