from playwright.sync_api import sync_playwright, expect

def test_save_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        context.add_cookies([
            {
                "name": "session",
                "value": "logged_in",
                "url": "http://localhost:8000"
            }
        ])

        context.storage_state(path="auth.json")

        browser.close()

def test_load_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        context = browser.new_context(storage_state="auth.json")

        page = context.new_page()
        page.goto("http://localhost:8000/api_test.html")

        cookies = context.cookies()
        print("Saved cookies:", cookies)

        assert any(
            cookie["name"] == "session"
            and cookie["value"] == "logged_in"
            for cookie in cookies
        )

        browser.close()
