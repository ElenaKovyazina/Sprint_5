import random


def generate_random_data_for_success_registration():
    new_name = f'Elena{random.randint(100,999)}'
    new_email = f'Elena_Suslova_{random.randint(100,999)}@mail.ru'
    new_password = f'pass{random.randint(100,999999)}'
    return new_name, new_email, new_password

def generate_random_data_for_bad_registration():
    new_name = f'Elena{random.randint(100,999)}'
    new_email = f'Elena{random.randint(100,999)}@mail.ru'
    new_password = f'{random.randint(10,999)}'
    return new_name, new_email, new_password