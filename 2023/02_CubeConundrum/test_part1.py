from unittest import TestCase

from part1 import solve


class Test(TestCase):
    def test_find_value(self):
        for line, expected in (
                ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 1),
                ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 2),
                ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 0),
                ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 0),
                ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', 5),
        ):
            with self.subTest(line=line, expected=expected):
                self.assertEqual(solve(line, 12, 13, 14), expected)
