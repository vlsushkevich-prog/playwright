import pytest
import enum
from playwright.sync_api import Page, expect


class ProgrammingLanguages(enum.Enum):
    PYTHON = 'Python'
    JAVA = 'Java'
    JAVASCRIPT = 'JavaScript'
    RUBY = 'Ruby'
    SHARP = 'C#'


@pytest.mark.parametrize('value', (x.value for x in ProgrammingLanguages))
def test_single_select(page: Page, value: str) -> None:
    page.goto('https://www.qa-practice.com/elements/select/single_select')
    page.locator('#id_choose_language').select_option(value)
    page.locator('#submit-id-submit').click()

    expect(page.locator('#result-text')).to_have_text(value)

