import unittest
import sys
sys.path.append(r'..\password-checker')
import password_checker


class password_check (unittest.TestCase):

    test_password = "password123"
    hashed_test = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
    hash_test_head = "CBFDA"
    hash_test_tail = "C6008F9CAB4083784CBD1874F76618D2A97"
    test_leaks_count = "294857"

    def test_if_password_received_is_correctly_hashed(self):
        expected_value = self.hashed_test
        actual_result = password_checker.password_hasher(self.test_password)

        self.assertEqual(expected_value, actual_result)

    def test_if_split_values_digits_are_returned(self):
        expected_first = self.hash_test_head
        expected_last = self.hash_test_tail
        first_part, last_part = password_checker.split_hash(
            self.hashed_test)

        self.assertEqual(expected_first, first_part)
        self.assertEqual(expected_last, last_part)

    def test_if_its_connecting_to_api(self):
        expected_value = 200
        actual_result = password_checker.request_api_data(self.hash_test_head)

        self.assertEqual(expected_value, actual_result.status_code)

    def test_if_correct_message_is_returned_when_NO_leaks_are_detected(self):
        test_input = 'thisShouldNot_beLeaked'
        expected_value = f'the password {test_input} was NOT leaked. Keep it going!'
        actual_result = password_checker.pwned_password_checker(test_input)

        self.assertEqual(expected_value, actual_result)
    
    def test_if_correct_message_is_returned_when_leaks_ARE_detected(self):
        expected_value = f'the password {self.test_password} was leaked {self.test_leaks_count} times. Maybe change that?'
        actual_result = password_checker.pwned_password_checker(self.test_password)

        self.assertEqual(expected_value, actual_result)


if __name__ == '__main__':
    unittest.main()
