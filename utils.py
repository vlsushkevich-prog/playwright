import string
import random


def generate_valid_text(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits + '-' + '_', k=length))

def generate_invalid_text(length: int) -> str:
    return ''.join(random.sample('!@#$%^&*()+=~`?/.,<>', k=length))