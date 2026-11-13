import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_page_loads(page):
    login_page = LoginPage(page)

    login_page.open()

    expect(login_page.username).to_be_visible()
    expect(login_page.password).to_be_visible()
    expect(login_page.login_button).to_be_visible()
