import unittest
import sys
sys.path.append('..\password-checker')
import password_checker

class password_hasher (unittest.TestCase):
  
  def test_should_hash_password_received(self):
    expected_value = "CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
    test_input = "password123"
    actual_result = password_checker.password_hasher(test_input)

    self.assertEquals(expected_value, actual_result)


if __name__ == '__main__':
    unittest.main()