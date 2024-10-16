import sys
import requests
from hashlib import sha1

def password_hasher(user_input):
  password = str(user_input)
  hash = sha1(password.encode('utf-8'))
  return hash.hexdigest().upper()

def get_first_five_hashed_characters(hashed_password):
  shortened_hash = hashed_password[:5]
  return shortened_hash

def api_url_constructor(short_hashcode):
  base_url = 'https://api.pwnedpasswords.com/range/'
  return f'{base_url}{short_hashcode}'

if __name__ == "__main__":
  passwords = sys.argv[1]
  hashed_password = password_hasher(passwords)
  shortened = get_first_five_hashed_characters(hashed_password)

  url = api_url_constructor(shortened)
  res = requests.get(url)

  print(res)