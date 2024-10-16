import sys
from hashlib import sha1

def password_hasher(user_input):
  password = str(user_input)
  hash = sha1(password.encode('utf-8'))
  return hash.hexdigest().upper()

def get_first_five_digits(user_password):
  shortened_hash = password_hasher(user_password)[:5]
  return shortened_hash

def api_url_constructor(user_password):
  base_url = 'https://api.pwnedpasswords.com/range/'
  shortened_hash = get_first_five_digits(user_password)

  return f'{base_url}{shortened_hash}'

if __name__ == "__main__":
  passwords = sys.argv[1]
  new_passcode = get_first_five_digits(passwords)

  print(new_passcode)