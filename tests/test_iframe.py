from playwright.sync_api import Page, expect


def test_iframe(page: Page) -> None:
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    new_page = page.frame_locator('iframe')
    element = new_page.locator('//span[@class="navbar-toggler-icon"]')
    element.click()
