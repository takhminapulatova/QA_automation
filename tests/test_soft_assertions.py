from playwright.sync_api import sync_playwright, expect
import pytest_check as check

def test_soft_assertions():
    username = "Takhmina"
    age = 30
    city = "Austin"

    check.equal(username, "Takhmina")
    print("Check 1 completed")

    check.equal(age, 30)
    print("Check 2 completed")

    check.equal(city, "Austin")
    print("Check 3 completed")

def test_multiple_page_checks():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        with check.check:
            expect(page).to_have_title("Wrong Title")

        print("First assertion completed")

        with check.check:
            expect(page.locator("h1")).to_have_text("Example Domain")

        print("Second assertion completed")

        browser.close()
