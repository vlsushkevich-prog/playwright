from playwright.sync_api import expect
from pages.practice_form_page import PracticeFormPage


def test_form_submit(practice_page, practice_form_test_data) -> None:
    practice_page.open_practice_form()
    practice_page.input_firstname(practice_form_test_data.FIRSTNAME)
    practice_page.input_lastname(practice_form_test_data.LASTNAME)
    practice_page.input_email(practice_form_test_data.EMAIL)
    practice_page.select_gender(practice_form_test_data.GENDER)
    practice_page.input_mobile(practice_form_test_data.MOBILE_NUMBER)
    practice_page.select_subjects('s')
    practice_page.select_hobbies(practice_form_test_data.HOBBIES)
    practice_page.select_picture(practice_form_test_data.PICTURE)
    practice_page.input_address(practice_form_test_data.ADDRESS)
    practice_page.select_state(practice_form_test_data.STATE)
    practice_page.select_city(practice_form_test_data.CITY)
    practice_page.submit_form()

    expect(practice_page._results_modal).to_be_visible()
    expect(practice_page._result_name).to_have_text('Homer Simpson')
    expect(practice_page._result_email).to_have_text(practice_form_test_data.EMAIL)
    expect(practice_page._result_gender).to_have_text(practice_form_test_data.GENDER)
    expect(practice_page._result_mobile).to_have_text(practice_form_test_data.MOBILE_NUMBER)
    expect(practice_page._result_birthday).to_have_text('2026-02-19')
    expect(practice_page._result_subjects).to_have_text('Social Studies')
    expect(practice_page._result_hobbies).to_have_text('Sports, Reading, Music')
    expect(practice_page._result_picture).to_have_text('homer-simpson-doughnuts.webp')
    expect(practice_page._result_address).to_have_text(practice_form_test_data.ADDRESS)
    expect(practice_page._result_state_and_city).to_have_text('Rajasthan')


