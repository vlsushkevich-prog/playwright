from playwright.sync_api import Page


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self._firstname_input = page.locator('//input[@name="first_name"]')
        self._lastname_input = page.locator('//input[@name="last_name"]')
        self._email_input = page.locator('//input[@name="email"]')
        self._gender_male_radio = page.locator('//*[@type="radio" and @value="Male"]')
        self._gender_female_radio = page.locator('//*[@type="radio" and @value="Female"]')
        self._gender_other_radio = page.locator('//*[@type="radio" and @value="Other"]')
        self._mobile_number_input = page.locator('//input[@name="mobile"]')
        self._birthday_picker = page.locator('//input[@name="date_of_birth"]')
        self._subjects_input = page.locator('//input[@id="subjectsAutocomplete"]')
        self._subject_suggestions_input = page.locator('#subjectsAutocomplete')
        self._hobbies_sport_checkbox = page.get_by_label('Sports')
        self._hobbies_reading_checkbox = page.get_by_label('Reading')
        self._hobbies_music_checkbox = page.get_by_label('Music')
        self._image_picker = page.locator('//input[@type="file" and @name="picture"]')
        self._address_input = page.locator('//textarea[@name="current_address"]')
        self._state_dropdown = page.locator('#div_id_state .custom-dropdown-control')
        self._city_dropdown = page.locator('#div_id_city .custom-dropdown-control')
        self._submit_button = page.get_by_role('button', name='Submit')

        self._results_modal = page.locator('#resultsModal')
        self._result_name = page.locator('tr:has-text("Student Name") td:nth-child(2)')
        self._result_email = page.locator('tr:has-text("Student Email") td:nth-child(2)')
        self._result_gender = page.locator('tr:has-text("Gender") td:nth-child(2)')
        self._result_mobile = page.locator('tr:has-text("Mobile") td:nth-child(2)')
        self._result_birthday = page.locator('tr:has-text("Date of Birth") td:nth-child(2)')
        self._result_subjects = page.locator('tr:has-text("Subjects") td:nth-child(2)')
        self._result_hobbies = page.locator('tr:has-text("Hobbies") td:nth-child(2)')
        self._result_picture = page.locator('tr:has-text("Picture") td:nth-child(2)')
        self._result_address = page.locator('tr:has-text("Address") td:nth-child(2)')
        self._result_state_and_city = page.locator('tr:has-text("State and City") td:nth-child(2)')

    def open_practice_form(self) -> None:
        self.page.goto('https://www.qa-practice.com/forms/practice-form')

    def input_firstname(self, firstname: str) -> None:
        self._firstname_input.fill(firstname)

    def input_lastname(self, lastname: str) -> None:
        self._lastname_input.fill(lastname)

    def input_email(self, email: str) -> None:
        self._email_input.fill(email)

    def select_gender(self, gender) -> None:
        match gender:
            case 'Male':
                self._gender_male_radio.click()
            case 'Female':
                self._gender_female_radio.click()
            case 'Other':
                self._gender_other_radio.click()

    def input_mobile(self, mobile: str) -> None:
        self._mobile_number_input.fill(mobile)

    def select_birthday(self, birthday: str) -> None:
        pass

    def select_subjects(self, subject: str) -> None:
        self._subject_suggestions_input.fill(subject)
        self.page.locator('.suggestion-item', has_text='Social Studies').click()

    def select_hobbies(self, hobbies: list) -> None:
        if 'Sports' in hobbies:
            self._hobbies_sport_checkbox.check()
        if 'Reading' in hobbies:
            self._hobbies_reading_checkbox.check()
        if 'Music' in hobbies:
            self._hobbies_music_checkbox.check()

    def select_picture(self, picture_path: str) -> None:
        with self.page.expect_file_chooser() as fc:
            self._image_picker.click()

        file_chooser = fc.value
        file_chooser.set_files(picture_path)

    def input_address(self, address: str) -> None:
        self._address_input.fill(address)

    def select_state(self, state: str) -> None:
        self._state_dropdown.click()
        self.page.locator(f'[data-value={state}]').click()

    def select_city(self, city: str) -> None:
        self._city_dropdown.click()
        self.page.locator(f'[data-value={city}]').click()

    def submit_form(self) -> None:
        self._submit_button.click()



