import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
def test_login_page_loads(page):
    page.goto("https://the-internet.herokuapp.com/login")

    expect(page.get_by_label("Username")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
