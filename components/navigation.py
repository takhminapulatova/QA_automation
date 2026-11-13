class Navigation:
    def __init__(self, page):
        self.page = page
        self.logout_button = page.locator("a[href='/logout']")

    def logout(self):
        self.logout_button.click()
