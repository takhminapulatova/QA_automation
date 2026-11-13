from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_successful_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

def test_login_and_logout(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    home_page.verify_logged_in()
    home_page.logout()

    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
