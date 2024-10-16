import unittest
import sys
sys.path.append('..\password-checker')
import password_checker

class password_check (unittest.TestCase):
  
  def test_if_password_received_is_correctly_hashed(self):
    expected_value = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
    test_input = "password123"
    actual_result = password_checker.password_hasher(test_input)

    self.assertEqual(expected_value, actual_result)

  def test_if_first_five_digits_are_returned(self):
    expected_value = "CBFDA"
    test_input = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
    actual_result = password_checker.get_first_five_hashed_characters(test_input)

    self.assertEqual(expected_value, actual_result)

  def test_if_url_built_correctly(self):
    expected_value = 'https://api.pwnedpasswords.com/range/CBFDA'
    test_input = "CBFDA"
    actual_result = password_checker.api_url_constructor(test_input)

    self.assertEqual(expected_value, actual_result)


if __name__ == '__main__':
    unittest.main()