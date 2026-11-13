from pages.base_page import BasePage

class TablePage(BasePage):
    URL = "https://the-internet.herokuapp.com/challenging_dom"

    def open(self):
        self.navigate(self.URL)

    def open_data_tables(self):
        self.navigate("https://the-internet.herokuapp.com/tables")

    def get_row_count(self):
        return self.page.locator("table tbody tr").count()

    def get_row_by_last_name(self, last_name):
        return self.page.locator("#table1 tbody tr").filter(
            has_text=last_name
        )

    def get_column_index(self, column_name):
        header = self.page.locator("#table1 thead th")

        for index in range(header.count()):
            if header.nth(index).inner_text().strip() == column_name:
                return index

        raise ValueError(f"Column not found: {column_name}")
