import pytest
from playwright.sync_api import Page
from pages.input_page import InputPage


@pytest.fixture
def input_page(page: Page):
     return InputPage(page)