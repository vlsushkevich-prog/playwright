from playwright.sync_api import Page,expect


def test_alert(page: Page) -> None:
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')

    def handle_alert(dialog) -> None:
        dialog.accept()

    page.on('dialog', handle_alert)
    page.get_by_text('Click for JS Alert').click()
    expect(page.locator('#result'), 'You successfully clicked an alert')

def test_alert_confirm(page: Page) -> None:
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    page.on('dialog', lambda dialog: dialog.accept())
    page.get_by_text('Click for JS Confirm').click()

    expect(page.locator('#result'), 'You clicked: Ok')

def test_alert_dismiss(page: Page) -> None:
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    page.on('dialog', lambda dialog: dialog.dismiss())
    page.get_by_text('Click for JS Confirm').click()

    expect(page.locator('#result'), 'You clicked: Cancel')

def test_alert_promt(page: Page) -> None:
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    page.on('dialog', lambda dialog: dialog.accept('text'))
    page.get_by_text('Click for JS Prompt').click()

    expect(page.locator('#result'), 'You entered: text')

def test_popup(page: Page) -> None:
    page.goto('https://www.qa-practice.com/elements/popup/modal')
    page.locator('#content > button').click()
    popup = page.locator('#content')
    popup.locator('#id_checkbox_0').check()
    popup.get_by_role('button', name='Send').click()

    expect(page.locator('#result-text'), 'select me or not')

def test_new_tab(context) -> None:
    page = context.new_page()
    page.goto('https://www.qa-practice.com/elements/new_tab/link')

    with context.expect_page() as new_page_info:
        page.locator('#new-page-link').click()

    new_tab = new_page_info.value
    expect(new_tab.locator('#result-text'), 'I am a new page in a new tab')


