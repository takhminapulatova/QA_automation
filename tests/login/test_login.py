from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.smoke
def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        page.get_by_label("Username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")

        page.get_by_role("button", name="Login").click()

        expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

        browser.close()

@pytest.mark.regression
def test_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("WrongPassword123")

        page.get_by_role("button", name="Login").click()

        expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

        browser.close()
