from playwright.sync_api import sync_playwright, expect

def test_add_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

        for i in range(3):
            page.get_by_role("button", name="Add Element").click()

        expect(page.get_by_role("button", name="Delete")).to_have_count(3)

        page.get_by_role("button", name="Delete").first.click()

        expect(page.get_by_role("button", name="Delete")).to_have_count(2)

        browser.close()
