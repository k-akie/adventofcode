from unittest import TestCase

from part1 import find_value


class Test(TestCase):
    def test_find_value(self):
        for line, expected in (
                ('1abc2', 12),
                ('pqr3stu8vwx', 38),
                ('a1b2c3d4e5f', 15),
                ('treb7uchet', 77),
        ):
            with self.subTest(line=line, expected=expected):
                self.assertEqual(find_value(line), expected)
