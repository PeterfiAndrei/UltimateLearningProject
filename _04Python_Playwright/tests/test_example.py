from playwright.sync_api import Page


def test_homepage_title(page: Page):
    page.goto("https://playwright.dev")
    assert (
        page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"
    )
