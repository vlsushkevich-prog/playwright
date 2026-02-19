from utils import *


class TestDataPracticeForm:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.email = None
        self.gender = None
        self.phone_number = None
        self.subject_start_letter = None
        self.hobbies = None
        self.address = None
        self.state = None
        self.city = None
        self.picture = 'test_data/homer-simpson-doughnuts.webp'

    def generate_random_data(self, firstname_len, lastname_len, email_len, address_len):
        self.firstname = self.generate_valid_name(firstname_len)
        self.lastname = self.generate_valid_name(lastname_len)
        self.email = self.generate_valid_email(email_len)
        self.gender = self.pick_random_gender()
        self.phone_number = self.generate_valid_phone_number()
        self.subject_start_letter = self.generate_subject_start_letter()
        self.hobbies = self.pick_random_hobbies()
        self.address = self.generate_valid_address(address_len)
        self.state = self.pick_random_state()
        self.city = self.pick_random_city(self.state)
        return self

    @staticmethod
    def generate_valid_name(length: int) -> str:
        return ''.join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def generate_valid_address(length: int) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))

    @staticmethod
    def generate_valid_email(length: int) -> str:
        prefix = ''.join(random.choices(string.ascii_letters, k=length))
        return f'{prefix}@mail.com'

    @staticmethod
    def pick_random_gender() -> str:
        genders = ['Male', 'Female', 'Other']
        return random.choice(genders)

    @staticmethod
    def generate_valid_phone_number() -> str:
        phone_code = '029'
        return phone_code + ''.join(random.choices(string.digits, k=7))

    @staticmethod
    def generate_subject_start_letter() -> str:
        return random.choice('epashcbm')

    @staticmethod
    def pick_random_hobbies() -> list:
        hobbies = ['Sports', 'Reading', 'Music']
        amount = random.randint(1, 3)
        return sorted(random.sample(hobbies, k=amount), key=lambda x: hobbies.index(x))

    @staticmethod
    def pick_random_state() -> str:
        states = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
        return random.choice(states)

    @staticmethod
    def pick_random_city(state: str) -> str:
        cities_map = {
            'NCR': ['Delhi', 'Gurgaon', 'Noida'],
            'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
            'Haryana': ['Karnal', 'Panipat'],
            'Rajasthan': ['Jaipur', 'Jaiselmer']
        }
        cities = cities_map.get(state)
        if not cities:
            raise ValueError(f'Unknown state: {state}')
        return random.choice(cities)
