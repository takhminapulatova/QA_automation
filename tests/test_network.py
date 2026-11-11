from playwright.sync_api import sync_playwright, expect

def test_mock_api_error():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.route(
            "**/json",
            lambda route: route.fulfill(
                status=500,
                body="Internal Server Error"
            )
        )

        response = page.goto("https://httpbin.org/json")

        print("Response status:", response.status)

        assert response.status == 500

        browser.close()

def test_product_api_error():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.route(
            "**/api/products",
            lambda route: route.fulfill(status=500)
        )

        page.goto("http://localhost:8000/api_test.html")

        page.get_by_role("button", name="Load Products").click()

        expect(page.locator("#message")).to_have_text("Unable to load products")

        browser.close()
