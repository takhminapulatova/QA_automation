from playwright.sync_api import expect
from pages.alerts_page import AlertsPage

def test_js_alert(page):
    alert_page = AlertsPage(page)
    alert_page.open()

    def handle_dialog(dialog):
        assert dialog.message == "I am a JS Alert"
        dialog.accept()

    page.once("dialog", handle_dialog)

    alert_page.click_js_alert()

    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

def test_js_confirm_accept(page):
    alerts_page = AlertsPage(page)
    alerts_page.open()

    def handle_dialog(dialog):
        assert dialog.message == "I am a JS Confirm"
        dialog.accept()

    page.once("dialog", handle_dialog)

    alerts_page.click_js_confirm()

    expect(page.locator("#result")).to_have_text("You clicked: Ok")

def test_js_confirm_dismiss(page):
    alerts_page = AlertsPage(page)
    alerts_page.open()

    def handle_dialog(dialog):
        assert dialog.message == "I am a JS Confirm"
        dialog.dismiss()

    page.once("dialog", handle_dialog)

    alerts_page.click_js_confirm()

    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

def test_js_prompt(page):
    alerts_page = AlertsPage(page)
    alerts_page.open()

    def handle_dialog(dialog):
        assert dialog.message == "I am a JS prompt"
        dialog.accept("Hello Playwright!")

    page.once("dialog", handle_dialog)

    alerts_page.click_js_prompt()

    expect(page.locator("#result")).to_have_text("You entered: Hello Playwright!")
