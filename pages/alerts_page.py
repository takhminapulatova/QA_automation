from pages.base_page import BasePage

class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def open(self):
        self.navigate(self.URL)

    def click_js_alert(self):
        self.page.get_by_role("button", name="Click for JS Alert").click()

    def click_js_confirm(self):
        self.page.get_by_role("button", name="Click for JS Confirm").click()

    def click_js_prompt(self):
        self.page.get_by_role("button", name="Click for JS Prompt").click()
