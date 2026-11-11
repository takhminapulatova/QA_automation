from playwright.sync_api import sync_playwright, expect

def test_trace():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            record_video_dir="videos/"
        )

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        try:
            page.goto("https://example.com")
            expect(page).to_have_title("Example Domain")

        finally:
            context.tracing.stop(path="trace.zip")
            context.close()
            browser.close()
