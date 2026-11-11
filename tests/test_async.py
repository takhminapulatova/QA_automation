import asyncio
from playwright.async_api import async_playwright


async def open_website():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://example.com")
        print(await page.title())

        await browser.close()

def test_async_browser():
    asyncio.run(open_website())
