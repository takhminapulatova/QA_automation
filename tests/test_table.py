from playwright.sync_api import sync_playwright, expect
from pages.table_page import TablePage

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

def test_table_row_count(page):
    table_page = TablePage(page)
    table_page.open()

    row_count = table_page.get_row_count()

    assert row_count == 10

def test_smith_using_pom(page):
    table_page = TablePage(page)
    table_page.open_data_tables()

    row = table_page.get_row_by_last_name("Smith")

    expect(row.locator("td").nth(0)).to_have_text("Smith")
    expect(row.locator("td").nth(1)).to_have_text("John")
    expect(row.locator("td").nth(2)).to_have_text("jsmith@gmail.com")

def test_smith_email_by_column_name(page):
    table_page = TablePage(page)
    table_page.open_data_tables()

    row = table_page.get_row_by_last_name("Smith")

    email_index = table_page.get_column_index("Email")

    email_cell = row.locator("td").nth(email_index)

    expect(email_cell).to_have_text("jsmith@gmail.com")
