
import unittest
from main import analyze_password


class TestPasswordAnalyzer(unittest.TestCase):

    def test_empty_password(self):
        with self.assertRaises(ValueError):
            analyze_password("")

    def test_common_password(self):
        result = analyze_password("password")
        self.assertTrue(result["is_common"])

    def test_repeated_characters(self):
        result = analyze_password("aaaa1234")
        self.assertTrue(result["repeated"])

    def test_predictable_pattern(self):
        result = analyze_password("12345678")
        self.assertTrue(result["has_pattern"])

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

    def test_unicode_password(self):
        result = analyze_password("你好你好")
        self.assertEqual(result["entropy"], 0)

    # Advanced pattern detection tests

    def test_ascending_sequence(self):
        result = analyze_password("abcd1234")
        self.assertTrue(result["has_pattern"])

    def test_descending_sequence(self):
        result = analyze_password("4321abcd")
        self.assertTrue(result["has_pattern"])

    def test_repeated_block_pattern(self):
        result = analyze_password("abababXY9!")
        self.assertTrue(result["has_pattern"])

    def test_random_pattern_not_detected(self):
        result = analyze_password("mK8!vT2#pQ")
        self.assertFalse(result["has_pattern"])

    def test_score_range(self):
        result = analyze_password("mK8!vT2#pQ")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 100)

    def test_common_password_gets_zero_score(self):
        result = analyze_password("password")
        self.assertEqual(result["score"], 0)


if __name__ == "__main__":
    unittest.main()
