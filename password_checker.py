import sys
from hashlib import sha1
import requests


def password_hasher(user_input):
    password = str(user_input)
    hashed = sha1(password.encode('utf-8'))

    return hashed.hexdigest().upper()


def get_first_five_hashed_characters(hashed_password):
    shortened_hash = hashed_password[:5]

    return shortened_hash


def request_api_data(hash_word):
    short_hashcode = get_first_five_hashed_characters(hash_word)
    request_url = f'https://api.pwnedpasswords.com/range/{short_hashcode}'

    res = requests.get(request_url)

    if res.status_code != 200:
        raise RuntimeError(f'Connection error, status {
                           res.status_code}. Check API and try again.')

    return res.status_code


if __name__ == "__main__":
    passwords = sys.argv[1]
    HASHED = password_hasher(passwords)
    response_code = request_api_data(HASHED)

    print(response_code)
