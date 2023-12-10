from unittest import TestCase

from part1 import solve, pre


class Test(TestCase):
    def test_pre(self):
        for line, expected in (
                ("467..114..", []),
                ("...*......", [3]),
                ("..35..633.", []),
                ("......#...", [6]),
                ("617*......", [3]),
                (".....+.58.", [5]),
                ("..592.....", []),
                ("......755.", []),
                ("...$.*....", [3, 5]),
                (".664.598..", []),
        ):
            with self.subTest(line=line, expected=expected):
                self.assertEqual(pre(line), expected)

    def test_solve(self):
        symbols = [
            [],
            [3],
            [],
            [6],
            [3],
            [5],
            [],
            [],
            [3, 5],
            [],
        ]
        for num, line, expected in (
            (0, "467..114..", 467),
            (1, "...*......", 0),
            (2, "..35..633.", 35 + 633),
            (3, "......#...", 0),
            (4, "617*......", 617),
            (5, ".....+.58.", 0),
            (6, "..592.....", 592),
            (7, "......755.", 755),
            (8, "...$.*....", 0),
            (9, ".664.598..", 664 + 598),
        ):
            with self.subTest(num=num, line=line, expected=expected):
                self.assertEqual(solve(num, line, symbols), expected)
