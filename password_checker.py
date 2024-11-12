import sys
from hashlib import sha1
import requests


def password_hasher(user_input):
    password = str(user_input)
    hashed = sha1(password.encode('utf-8'))

    return hashed.hexdigest().upper()


def split_hash(hashed_password):
    head = hashed_password[:5]
    tail = hashed_password[5:]

    return head, tail


def request_api_data(hash_head):
    request_url = f'https://api.pwnedpasswords.com/range/{hash_head}'

    res = requests.get(request_url)

    if res.status_code != 200:
        raise RuntimeError(f'Connection error, status {
                           res.status_code}. Check API and try again.')

    return res

def check_pwned_api(password):
    pass


if __name__ == "__main__":
    print('OK')
