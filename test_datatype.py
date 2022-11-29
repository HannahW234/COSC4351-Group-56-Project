import unittest
import datatype_check as dc

class MyTestCase(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_is_valid_name_is_true(self):
        self.assertTrue(dc.is_valid_name("Firstname Lastname"))

    def test_is_valid_name_is_false(self):
        self.assertFalse(dc.is_valid_name("Firstname00"))

    def test_is_valid_time_is_true(self):
        self.assertTrue(dc.is_valid_time('2022-12-31', '14:00'))

    def test_is_valid_time_is_false(self):
        self.assertFalse(dc.is_valid_time(dc.datetime.date.today(), '11:00'))

if __name__ == '__main__':
    unittest.main()
