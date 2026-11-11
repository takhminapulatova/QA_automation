from playwright.sync_api import sync_playwright

def test_browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context1 = browser.new_context()
        context2 = browser.new_context()

        page1 = context1.new_page()
        page2 = context2.new_page()

        page1.goto("https://example.com")
        page2.goto("https://example.com")

        print(page1.title())
        print(page2.title())

        context1.add_cookies([
            {
                "name": "username",
                "value": "tomsmith",
                "url": "https://example.com"
            }
        ])

        print("Context 1 cookies:", context1.cookies())
        print("Context 2 cookies:", context2.cookies())

        browser.close()
