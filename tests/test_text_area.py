from playwright.sync_api import Page, expect


def test_text_area(page: Page) -> None:
    page.goto('https://www.qa-practice.com/elements/textarea/single')
    page.locator(('#id_text_area')).fill('asdasdasd')
    page.get_by_role('button', name='Submit').click()

    expect(page.locator('.result-chapters')).to_have_text('asdasdasd')