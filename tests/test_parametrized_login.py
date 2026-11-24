import json
import pytest
from pathlib import Path
from playwright.sync_api import expect

# Locate the JSON file
DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "test_data"
    / "login_data.json"
)

# Load test data
with open(DATA_FILE, "r") as file:
    login_data = json.load(file)

@pytest.mark.parametrize("user", login_data)
def test_login(page, user):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill(user["username"])
    page.locator("#password").fill(user["password"])
    page.locator("#login-button").click()

    if user["should_login"]:
        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )
    else:
        expect(page.locator("[data-test='error']")).to_be_visible()