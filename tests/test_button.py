from playwright.sync_api import Page, expect


def test_button(page: Page) -> None:
    page.goto('https://www.qa-practice.com/elements/button/simple')
    page.get_by_role('button', name='Click').click()

    expect(page.locator('#result-text')).to_be_visible()
    expect(page.locator('#result-text')).to_have_text('Submitted')