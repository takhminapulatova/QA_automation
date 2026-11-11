from playwright.sync_api import sync_playwright, expect

def test_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dropdown")

        dropdown = page.locator("#dropdown")

        dropdown.select_option(label="Option 2")

        expect(dropdown).to_have_value("2")

        browser.close()
