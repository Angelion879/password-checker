import unittest
import sys
sys.path.append(r'..\password-checker')
import password_checker


class password_check (unittest.TestCase):

    def test_if_password_received_is_correctly_hashed(self):
        expected_value = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
        test_input = "password123"
        actual_result = password_checker.password_hasher(test_input)

        self.assertEqual(expected_value, actual_result)

    def test_if_split_values_digits_are_returned(self):
        expected_first = "CBFDA"
        expected_last = "C6008F9CAB4083784CBD1874F76618D2A97"
        test_input = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
        first_part, last_part = password_checker.split_hash(
            test_input)

        self.assertEqual(expected_first, first_part)
        self.assertEqual(expected_last, last_part)

    def test_if_its_connecting_to_api(self):
        expected_value = 200
        test_input = "CBFDA"
        actual_result = password_checker.request_api_data(test_input)

        self.assertEqual(expected_value, actual_result.status_code)


if __name__ == '__main__':
    unittest.main()
