from playwright.sync_api import sync_playwright, expect

def test_dynamic_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dynamic_controls")

        page.get_by_role("button", name="Remove").click()

        expect(page.get_by_role("button", name="Add")).to_be_visible()

        browser.close()
