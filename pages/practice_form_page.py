from playwright.sync_api import Page, expect

URL = 'https://www.qa-practice.com/forms/practice-form'

class PracticeFormPage:
    SUCCESS_FORM_SUBMIT_HEADER = 'Thanks for submitting the form'
    PHONE_NUMBER_VALIDATION_MESSAGE = 'Mobile number must be exactly 10 digits'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.firstname_input = page.locator('//input[@name="first_name"]')
        self.lastname_input = page.locator('//input[@name="last_name"]')
        self.email_input = page.locator('//input[@name="email"]')
        self.gender_male_radio = page.locator('//*[@type="radio" and @value="Male"]')
        self.gender_female_radio = page.locator('//*[@type="radio" and @value="Female"]')
        self.gender_other_radio = page.locator('//*[@type="radio" and @value="Other"]')
        self.phone_number_input = page.locator('//input[@name="mobile"]')
        self.birthday_picker = page.locator('//input[@name="date_of_birth"]')
        self.subject_suggestions_input = page.locator('#subjectsAutocomplete')
        self.subjects_option_first = page.locator('.suggestion-item').first
        self.image_picker = page.locator('//input[@type="file" and @name="picture"]')
        self.address_input = page.locator('//textarea[@name="current_address"]')
        self.state_dropdown = page.locator('#div_id_state .custom-dropdown-control')
        self.city_dropdown = page.locator('#div_id_city .custom-dropdown-control')
        self.submit_button = page.get_by_role('button', name='Submit')

        self.results_modal = page.locator('#resultsModal')
        self.results_modal_header = page.locator('.modal-title')
        self.result_name = page.locator('tr:has-text("Student Name") td:nth-child(2)')
        self.result_email = page.locator('tr:has-text("Student Email") td:nth-child(2)')
        self.result_gender = page.locator('tr:has-text("Gender") td:nth-child(2)')
        self.result_mobile = page.locator('tr:has-text("Mobile") td:nth-child(2)')
        self.result_birthday = page.locator('tr:has-text("Date of Birth") td:nth-child(2)')
        self.result_subjects = page.locator('tr:has-text("Subjects") td:nth-child(2)')
        self.result_hobbies = page.locator('tr:has-text("Hobbies") td:nth-child(2)')
        self.result_picture = page.locator('tr:has-text("Picture") td:nth-child(2)')
        self.result_address = page.locator('tr:has-text("Address") td:nth-child(2)')
        self.result_state_and_city = page.locator('tr:has-text("State and City") td:nth-child(2)')

        self.phone_number_validation = page.locator('#error_1_id_mobile')

    def open_practice_form(self) -> None:
        self.page.goto(URL)

    def input_firstname(self, firstname: str) -> None:
        self.firstname_input.fill(firstname)

    def input_lastname(self, lastname: str) -> None:
        self.lastname_input.fill(lastname)

    def input_email(self, email: str) -> None:
        self.email_input.fill(email)

    def select_gender(self, gender) -> None:
        match gender:
            case 'Male':
                self.gender_male_radio.click()
            case 'Female':
                self.gender_female_radio.click()
            case 'Other':
                self.gender_other_radio.click()
            case _:
                pass

    def input_mobile(self, phone_number: str) -> None:
        self.phone_number_input.fill(phone_number)

    def select_birthday(self, birthday: str) -> None:
        pass

    def select_subjects(self, subjects: list) -> None:
        for subject in subjects:
            self.subject_suggestions_input.fill(subject)
            if self.subjects_option_first.is_visible():
                self.subjects_option_first.click()
            else:
                pass

    def select_hobbies(self, hobbies: list) -> None:
        for hobby in hobbies:
            self.page.get_by_label(hobby).check()

    def select_picture(self, picture_path: str) -> None:
        with self.page.expect_file_chooser() as fc:
            self.image_picker.click()
        if picture_path:
            file_chooser = fc.value
            file_chooser.set_files(picture_path)
        else:
            pass

    def input_address(self, address: str) -> None:
        self.address_input.fill(address)

    def select_state(self, state: str) -> None:
        self.state_dropdown.click()
        self.page.locator(f'[data-value="{state}"]').click()

    def select_city(self, city: str) -> None:
        self.city_dropdown.click()
        self.page.locator(f'[data-value={city}]').click()

    def fill_form(self, user) -> None:
        self.input_firstname(user.firstname)
        self.input_lastname(user.lastname)
        self.input_email(user.email)
        self.select_gender(user.gender)
        self.input_mobile(user.phone_number)
        self.select_subjects(user.subjects)
        self.select_hobbies(user.hobbies)
        self.select_picture(user.picture)
        self.input_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)

    def submit_form(self) -> None:
        self.submit_button.click()

    def verify_form(self, user) -> None:
        expect(self.results_modal).to_be_visible()
        expect(self.results_modal_header).to_have_text(self.SUCCESS_FORM_SUBMIT_HEADER)
        expect(self.result_name).to_have_text(user.firstname + ' ' + user.lastname)
        expect(self.result_email).to_have_text(user.email)
        expect(self.result_gender).to_have_text(user.gender)
        expect(self.result_mobile).to_have_text(user.phone_number)
        expect(self.result_birthday).to_have_text('2026-02-20')
        expect(self.result_subjects).to_have_text(', '.join(user.subjects))
        expect(self.result_hobbies).to_have_text(', '.join(user.hobbies))
        expect(self.result_picture).to_have_text(user.picture.split('/')[-1])
        expect(self.result_address).to_have_text(user.address)
        expect(self.result_address).to_have_text(user.address)
        expect(self.result_state_and_city).to_have_text(user.state)

    def check_form_not_submitted(self) -> None:
        expect(self.results_modal).not_to_be_visible()

    def check_phone_number_validation(self) -> None:
        expect(self.phone_number_validation).to_have_text(self.PHONE_NUMBER_VALIDATION_MESSAGE)




