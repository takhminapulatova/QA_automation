from playwright.sync_api import sync_playwright
import pytest
from config import TestConfig

@pytest.fixture(scope="module")
def username():
    print("Creating username fixture")
    return "tomsmith"

@pytest.fixture(autouse=True)
def setup_test():
    print("Setting up test automatically")

@pytest.fixture
def page(request):
    browser_name = request.param

    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=True)
        page = browser.new_page()

        yield page

        browser.close()

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=["dev", "staging", "prod"],
        help="Select the testing environment"
    )
    parser.addoption(
        "--browser",
        action="append",
        default=[],
        choices=["chromium", "firefox", "webkit"],
        help="Select the browser"
    )

@pytest.fixture
def base_url(request):
    environment = request.config.getoption("--env")
    config = TestConfig(environment)
    return config.base_url

def pytest_generate_tests(metafunc):
    if "page" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browser")
        browsers = browsers or ["chromium"]

        metafunc.parametrize("page", browsers, indirect=True)