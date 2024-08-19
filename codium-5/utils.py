import random


def generate_random_id():
    return ''.join([str(random.randint(0, 9)) for _ in range(8)])


def validate_password(password):
    # TODO: Implement password validation
    return True
