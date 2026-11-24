from playwright.sync_api import expect

def test_mobile_viewport(page):
    page.set_viewport_size({
        "width": 390,
        "height": 844
    })

    page.goto("https://www.saucedemo.com")

    assert page.viewport_size["width"] == 390
    assert page.viewport_size["height"] == 844

    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#login-button")).to_be_visible()

    scroll_width = page.evaluate("document.documentElement.scrollWidth")
    client_width = page.evaluate("document.documentElement.clientWidth")

    assert scroll_width <= client_width, "Horizontal overflow detected"
