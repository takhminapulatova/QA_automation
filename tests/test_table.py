from playwright.sync_api import sync_playwright, expect

def test_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/tables")

        row = page.locator("#table1 tbody tr").filter(has_text="Smith")
        
        expect(row.locator("td").nth(0)).to_have_text("Smith")
        
        expect(row.locator("td").nth(1)).to_have_text("John")
        
        expect(row.locator("td").nth(2)).to_have_text("jsmith@gmail.com")
        
        browser.close()
        