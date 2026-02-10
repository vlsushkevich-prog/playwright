from playwright.sync_api import Page, expect


def test_checkbox(page: Page) -> None:
    page.goto('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    page.get_by_label('Select me or not').check()
    page.get_by_role('button', name='Submit').click()

    expect(page.locator('#result-text')).to_have_text('select me or not')