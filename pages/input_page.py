from playwright.sync_api import Page


class InputPage():
    MIN_VALIDATION_MESSAGE = 'Please enter 2 or more characters'
    MAX_VALIDATION_MESSAGE = 'Please enter no more than 25 characters'
    INVALID_CHAR_MESSAGE = ('Enter a valid string consisting of letters, numbers,'
                            ' underscores or hyphens.')

    def __init__(self, page: Page) -> None:
        self.page = page
        self._input_field = page.locator('#id_text_string')
        self._result_field = page.locator('#result-text')
        self._validation_message = page.locator('.invalid-feedback')

    def open_page(self) -> None:
        self.page.goto('https://www.qa-practice.com/elements/input/simple')

    def fill_input(self, value) -> None:
        self._input_field.fill(value)

    def submit(self) -> None:
        self._input_field.press('Enter')


