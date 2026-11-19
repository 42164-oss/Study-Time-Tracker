"""ทดสอบเงื่อนไขเวลาเรียนและการจำแนกประเภท"""

import unittest

from logic import classify_duration, validate_session


class ValidateSessionTests(unittest.TestCase):
    def test_required_durations(self) -> None:
        cases = [
            (0, False, None),
            (29, True, "Short"),
            (30, True, "Medium"),
            (59, True, "Medium"),
            (60, True, "Long"),
            (240, True, "Long"),
            (241, False, None),
        ]

        for minutes, expected_valid, expected_category in cases:
            with self.subTest(minutes=minutes):
                is_valid, _ = validate_session("คณิตศาสตร์", str(minutes))
                self.assertEqual(is_valid, expected_valid)
                if expected_valid:
                    self.assertEqual(classify_duration(minutes), expected_category)

    def test_rejects_empty_subject_and_non_integer_duration(self) -> None:
        self.assertFalse(validate_session("   ", "30")[0])
        self.assertFalse(validate_session("ภาษาไทย", "30.5")[0])
        self.assertFalse(validate_session("ภาษาไทย", "")[0])


if __name__ == "__main__":
    unittest.main()
