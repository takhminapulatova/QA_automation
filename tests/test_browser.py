from playwright.sync_api import sync_playwright, expect

def test_open():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://example.com")

        assert page.title() == "Example Domain"

        expect(
            page.get_by_text(
                "This domain is for use in documentation example",
                exact=False
            )
        ).to_be_visible()

        browser.close()
