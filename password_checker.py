import sys
from hashlib import sha1

def password_hasher(user_input):
  password = str(user_input)
  hash = sha1(password.encode('utf-8'))
  return hash.hexdigest().upper()

def get_first_five_digits(hashed_password):
  shortened_hash = password_hasher(hashed_password)[:5]
  return shortened_hash


if __name__ == "__main__":
  passwords = sys.argv[1]
  new_passcode = get_first_five_digits(passwords)

  print(new_passcode)