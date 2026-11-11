from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="module")
def username():
    print("Creating username fixture")
    return "tomsmith"

@pytest.fixture(autouse=True)
def setup_test():
    print("Setting up test automatically")

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()
