
import unittest

from main import analyze_password


class TestPasswordAnalyzer(unittest.TestCase):

    def test_empty_password(self):
        with self.assertRaises(ValueError):
            analyze_password("")

    def test_common_password(self):
        result = analyze_password("password")
        self.assertTrue(result["is_common"])
        self.assertEqual(result["strength"], "Very Weak")

    def test_repeated_characters(self):
        result = analyze_password("aaaa1111")
        self.assertTrue(result["repeated"])
        self.assertEqual(result["strength"], "Very Weak")

    def test_predictable_pattern(self):
        result = analyze_password("12345678")
        self.assertTrue(result["has_pattern"])
        self.assertEqual(result["strength"], "Very Weak")

    def test_lowercase_detection(self):
        result = analyze_password("hello123")
        self.assertTrue(result["lowercase"])

    def test_uppercase_detection(self):
        result = analyze_password("HELLO123")
        self.assertTrue(result["uppercase"])

    def test_digit_detection(self):
        result = analyze_password("hello123")
        self.assertTrue(result["digits"])

    def test_special_character_detection(self):
        result = analyze_password("hello@123")
        self.assertTrue(result["special"])

    def test_character_pool(self):
        result = analyze_password("hello123@")
        self.assertEqual(result["character_pool"], 68)

    def test_password_length(self):
        result = analyze_password("hello123")
        self.assertEqual(result["length"], 8)


if __name__ == "__main__":
    unittest.main()
