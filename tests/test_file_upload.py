from playwright.sync_api import sync_playwright, expect

def test_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/upload")

        page.locator("#file-upload").set_input_files("sample.txt")

        page.locator("#file-submit").click()

        file = page.locator("#uploaded-files")

        expect(file).to_have_text("sample.txt")

        browser.close()
