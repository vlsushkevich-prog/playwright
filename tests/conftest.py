import pytest
from playwright.sync_api import Page
from pages.input_page import InputPage
from pages.practice_form_page import PracticeFormPage
from test_data.practice_form_test_data import UserFactory


@pytest.fixture
def input_page(page: Page):
     return InputPage(page)

@pytest.fixture
def practice_page(page: Page):
    return PracticeFormPage(page)

@pytest.fixture
def user_factory():
    return UserFactory()