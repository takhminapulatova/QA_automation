from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")

    def open(self):
        self.navigate(self.URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
