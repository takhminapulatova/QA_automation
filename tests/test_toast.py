from playwright.sync_api import sync_playwright, expect
from pathlib import Path

def test_toast():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        toast_html = Path("toast.html").resolve().as_uri()
        page.goto(toast_html)

        page.get_by_role("button", name="Save").click()

        expect(page.locator("#toast")).to_be_visible(timeout=5000)

        expect(page.locator("#toast")).to_have_text("Saved successfully")

        browser.close()
