from unittest import TestCase

from part2 import sub_letter_first
from part2 import sub_letter_last
from part2 import find_first
from part2 import find_last


class Test(TestCase):
    def test_sub_letters(self):
        for line, expect1, expect2 in (
                ('two1nine', '21nine', 'two19'),
                ('eightwothree', '8wothree', 'eightwo3'),
                ('abcone2threexyz', 'abc12threexyz', 'abcone23xyz'),
                ('xtwone3four', 'x2ne3four', 'xtwone34'),
                ('4nineeightseven2', '49eightseven2', '4nineeight72'),
                ('zoneight234', 'z1ight234', 'zon8234'),
                ('7pqrstsixteen', '7pqrst6teen', '7pqrst6teen'),
        ):
            with self.subTest(line=line, expect1=expect1, expect2=expect2):
                self.assertEqual(sub_letter_first(line), expect1)
                self.assertEqual(sub_letter_last(line), expect2)

    def test_find_value(self):
        for line, expected in (
                ('two1nine', 29),
                ('eightwothree', 83),
                ('abcone2threexyz', 13),
                ('xtwone3four', 24),
                ('4nineeightseven2', 42),
                ('zoneight234', 14),
                ('7pqrstsixteen', 76),
        ):
            with self.subTest(line=line, expected=expected):
                result = find_first(line) + find_last(line)
                self.assertEqual(int(result), expected)

