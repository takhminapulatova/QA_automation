from playwright.sync_api import expect
from pages.base_page import BasePage
from components.navigation import Navigation

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.navigation = Navigation(page)

    def verify_logged_in(self):
        expect(self.navigation.logout_button).to_be_visible()

    def logout(self):
        self.navigation.logout()
