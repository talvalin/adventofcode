import unittest
import day04


class Day04Test(unittest.TestCase):
    
    def test_part1_examples(self):
        password1 = 111111
        password2 = 223450
        password3 = 123789

        self.assertTrue(day04.test_password(password1))
        self.assertFalse(day04.test_password(password2))
        self.assertFalse(day04.test_password(password3))

    def test_part2_examples(self):
        password1 = 112233
        password2 = 123444
        password3 = 111122

        self.assertTrue(day04.test_password_v2(password1))
        self.assertFalse(day04.test_password_v2(password2))
        self.assertTrue(day04.test_password_v2(password3))

if __name__ == "__main__":
    unittest.main()