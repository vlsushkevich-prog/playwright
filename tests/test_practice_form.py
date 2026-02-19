def test_form_submit(practice_page, user_factory) -> None:
    user = user_factory.generate_user()
    practice_page.open_practice_form()
    practice_page.fill_form(user)
    practice_page.submit_form()
    practice_page.verify_form(user)

def test_firstname_required_validation(practice_page, user_factory) -> None:
    user = user_factory.generate_user(firstname='')
    practice_page.open_practice_form()
    practice_page.fill_form(user)
    practice_page.submit_form()
    practice_page.check_form_not_submitted()

def test_lastname_required_validation(practice_page, user_factory) -> None:
    user = user_factory.generate_user(lastname='')
    practice_page.open_practice_form()
    practice_page.fill_form(user)
    practice_page.submit_form()
    practice_page.check_form_not_submitted()

def test_email_format_validation(practice_page, user_factory) -> None:
    user = user_factory.generate_user(email='sausage')
    practice_page.open_practice_form()
    practice_page.fill_form(user)
    practice_page.submit_form()
    practice_page.check_form_not_submitted()

def test_gender_required_validation(practice_page, user_factory) -> None:
    user = user_factory.generate_user(gender=None)
    practice_page.open_practice_form()
    practice_page.fill_form(user)
    practice_page.submit_form()
    practice_page.check_form_not_submitted()

def test_phone_number_len_validation(practice_page, user_factory) -> None:
    user = user_factory.generate_user(phone_number='123')
    practice_page.open_practice_form()
    practice_page.fill_form(user)
    practice_page.submit_form()
    practice_page.check_form_not_submitted()
    practice_page.check_phone_number_format_validation()