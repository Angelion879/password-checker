import sys
from hashlib import sha1

def password_hasher(user_input):
  password = str(user_input)
  hash = sha1(password.encode('utf-8'))
  return hash.hexdigest().upper()


if __name__ == "__main__":
  passwords = sys.argv[1]
  new_passcode = password_hasher(passwords)

  print(new_passcode)