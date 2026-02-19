import pytest
import random
from playwright.sync_api import expect
from utils import generate_valid_text, generate_invalid_text
from pages.input_page import InputPage


@pytest.mark.parametrize('value', [generate_valid_text(2) for _ in range(10)])
def test_input_min_value(input_page, value) -> None:
    input_page.open_page()
    input_page.fill_input(value)
    input_page.submit()

    expect(input_page._result_field).to_be_visible()
    expect(input_page._result_field).to_have_text(value)

@pytest.mark.parametrize('value', [generate_valid_text(25) for _ in range(10)])
def test_input_max_value(input_page, value) -> None:
    input_page.open_page()
    input_page.fill_input(value)
    input_page.submit()

    expect(input_page._result_field).to_be_visible()
    expect(input_page._result_field).to_have_text(value)

@pytest.mark.parametrize('value', [generate_valid_text(1) for _ in range(10)])
def test_input_min_validation(input_page, value) -> None:
    input_page.open_page()
    input_page.fill_input(value)
    input_page.submit()

    expect(input_page._result_field).not_to_be_visible()
    expect(input_page._validation_message).to_be_visible()
    expect(input_page._validation_message).to_have_text(InputPage.MIN_VALIDATION_MESSAGE)

@pytest.mark.parametrize('value', [generate_valid_text(26),
                                   generate_valid_text(100),
                                   generate_valid_text(1000)])
def test_input_max_validation(input_page, value) -> None:
    input_page.open_page()
    input_page.fill_input(value)
    input_page.submit()

    expect(input_page._result_field).not_to_be_visible()
    expect(input_page._validation_message).to_be_visible()
    expect(input_page._validation_message).to_have_text(InputPage.MAX_VALIDATION_MESSAGE)

@pytest.mark.parametrize('value', [generate_invalid_text(random.randint(2, 18)) for _ in range(10)])
def test_input_invalid_chars(input_page, value) -> None:
    input_page.open_page()
    input_page.fill_input(value)
    input_page.submit()

    expect(input_page._result_field).not_to_be_visible()
    expect(input_page._validation_message).to_be_visible()
    expect(input_page._validation_message).to_have_text(InputPage.INVALID_CHAR_MESSAGE)