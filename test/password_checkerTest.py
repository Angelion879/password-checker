import password_checker
import unittest
import sys
sys.path.append(r'..\password-checker')


class password_check (unittest.TestCase):

    def test_if_password_received_is_correctly_hashed(self):
        expected_value = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
        test_input = "password123"
        actual_result = password_checker.password_hasher(test_input)

        self.assertEqual(expected_value, actual_result)

    def test_if_first_five_digits_are_returned(self):
        expected_value = "CBFDA"
        test_input = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
        actual_result = password_checker.get_first_five_hashed_characters(
            test_input)

        self.assertEqual(expected_value, actual_result)

    def test_if_its_connecting_to_api(self):
        expected_value = 200
        test_input = "CBFDA"
        actual_result = password_checker.request_api_data(test_input)

        self.assertEqual(expected_value, actual_result)


if __name__ == '__main__':
    unittest.main()
