import sys
from hashlib import sha1
import requests


def password_hasher(password):
    password = str(password)
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

def check_api_data_for_password_leaks(api_hashes, hash_to_be_checked):
    cleaned_hashes = (line.split(':') for line in api_hashes.text.splitlines())

    for hashed, leak_count in cleaned_hashes:
        if hashed == hash_to_be_checked:
            return leak_count
    return 0

def pwned_password_checker(user_password):
    HASHED = password_hasher(user_password)
    heads, tails = split_hash(HASHED)

    pwned_api_data = request_api_data(heads)

    leaked_counter = check_api_data_for_password_leaks(pwned_api_data, tails)

    if leaked_counter:
        return(f'the password {user_password} was leaked {leaked_counter} times. Maybe change that?')
    else:
        return(f'the password {user_password} was NOT leaked. Keep it going!')

if __name__ == "__main__":
    passwords = sys.argv[1:]

    for p in passwords:
        print(pwned_password_checker(p))
    