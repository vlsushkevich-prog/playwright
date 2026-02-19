import pytest
from playwright.sync_api import Page
from pages.input_page import InputPage
from pages.practice_form_page import PracticeFormPage
from test_data.practice_form_test_data import TestDataPracticeForm


@pytest.fixture
def input_page(page: Page):
     return InputPage(page)

@pytest.fixture
def practice_page(page: Page):
    return PracticeFormPage(page)

@pytest.fixture
def practice_form_test_data():
    return TestDataPracticeForm().generate_random_data(firstname_len=8, lastname_len=8, email_len=8, address_len=50)
