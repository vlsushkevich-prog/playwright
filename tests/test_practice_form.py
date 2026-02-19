from playwright.sync_api import expect
from pages.practice_form_page import PracticeFormPage
import time


def test_form_submit(practice_page, practice_form_test_data) -> None:
    practice_page.open_practice_form()
    practice_page.input_firstname(practice_form_test_data.firstname)
    practice_page.input_lastname(practice_form_test_data.lastname)
    practice_page.input_email(practice_form_test_data.email)
    practice_page.select_gender(practice_form_test_data.gender)
    practice_page.input_mobile(practice_form_test_data.phone_number)
    practice_page.select_subjects(practice_form_test_data.subject_start_letter)
    practice_page.select_hobbies(practice_form_test_data.hobbies)
    practice_page.select_picture(practice_form_test_data.picture)
    practice_page.input_address(practice_form_test_data.address)
    practice_page.select_state(practice_form_test_data.state)
    practice_page.select_city(practice_form_test_data.city)
    practice_page.submit_form()
    time.sleep(5)

    expect(practice_page._results_modal).to_be_visible()
    expect(practice_page._result_name).to_have_text(practice_form_test_data.firstname + ' ' + practice_form_test_data.lastname)
    expect(practice_page._result_email).to_have_text(practice_form_test_data.email)
    expect(practice_page._result_gender).to_have_text(practice_form_test_data.gender)
    expect(practice_page._result_mobile).to_have_text(practice_form_test_data.phone_number)
    expect(practice_page._result_birthday).to_have_text('2026-02-19')
    expect(practice_page._result_subjects).to_have_text(practice_page._subject_name)
    expect(practice_page._result_hobbies).to_have_text(', '.join(practice_form_test_data.hobbies))
    expect(practice_page._result_picture).to_have_text('homer-simpson-doughnuts.webp')
    expect(practice_page._result_address).to_have_text(practice_form_test_data.address)
    expect(practice_page._result_state_and_city).to_have_text(practice_form_test_data.state)
    time.sleep(20)



