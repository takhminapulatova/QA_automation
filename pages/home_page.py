from playwright.sync_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logout_button = page.locator("a[href='/logout']")

    def verify_logged_in(self):
        expect(self.logout_button).to_be_visible()

    def logout(self):
        self.logout_button.click()
