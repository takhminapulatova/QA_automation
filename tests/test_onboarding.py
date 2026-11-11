from playwright.sync_api import sync_playwright, expect
from pathlib import Path

def test_onboarding():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        html_file = Path("onboarding.html").resolve().as_uri()
        page.goto(html_file)

        page.get_by_label("Employee name").fill("Takhmina")

        department_dropdown = page.locator("#department")

        department_dropdown.select_option(label="QA")

        document = page.locator("#document")

        document.set_input_files("sample.txt")

        page.get_by_role("button", name="Submit").click()

        expect(page.locator("#result")).to_have_text("Onboarding Complete")

        browser.close()
