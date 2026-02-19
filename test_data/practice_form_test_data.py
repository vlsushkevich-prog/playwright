from faker import Faker
import random
import os
from dataclasses import dataclass


fake = Faker()

@dataclass
class User:
    firstname: str
    lastname: str
    email: str
    gender: str
    phone_number: str
    address: str
    subjects: list
    hobbies: list
    state: str
    city: str
    picture: str

class UserFactory:
    CITIES_MAPPING = {
            'NCR': ['Delhi', 'Gurgaon', 'Noida'],
            'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
            'Haryana': ['Karnal', 'Panipat'],
            'Rajasthan': ['Jaipur', 'Jaiselmer']
    }
    GENDERS = ['Male', 'Female', 'Other']
    HOBBIES = ['Sports', 'Reading', 'Music']
    SUBJECTS = ['Chemistry', 'English', 'Arts', 'Sanskrit']
    IMAGES_PATH = os.path.join(os.path.dirname(__file__), 'images')

    @classmethod
    def generate_user(cls, **kwargs) -> User:
        state = kwargs.get('state') or random.choice(list(cls.CITIES_MAPPING.keys()))
        city = kwargs.get('city') or random.choice(cls.CITIES_MAPPING[state])
        user_data = {
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'email': fake.email(),
            'gender': random.choice(cls.GENDERS),
            'phone_number': fake.numerify('029#######'),
            'address': fake.address(),
            'subjects': random.sample(cls.SUBJECTS, random.randint(1, 4)),
            'hobbies': sorted(random.sample(cls.HOBBIES, k=random.randint(1, 3)),
                              key=lambda x: cls.HOBBIES.index(x)),
            'picture': random.choice([os.path.join(cls.IMAGES_PATH, f) for f in os.listdir(cls.IMAGES_PATH)]),
            'state': state,
            'city': city
        }

        user_data.update(kwargs)
        return User(**user_data)