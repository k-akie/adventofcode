import re


def solve(_line: str, _red: int, _green: int, _blue: int) -> int:
    bag = {
        'red': _red,
        'green': _green,
        'blue': _blue
    }

    result = re.compile(r'Game (\d+): (.*)').match(_line).groups()
    game = int(result[0])
    cubes = re.split('[,;]', result[1])

    regex = re.compile(r'\s?(\d+) (.*)')
    for cube in cubes:
        s_num,  name = regex.match(cube).groups()
        num = int(s_num)
        if bag[name] < num:
            return 0

    return game


if __name__ == '__main__':
    red = 12
    green = 13
    blue = 14

    total = 0
    with open('input.txt') as file:
        for s_line in file:
            total += solve(s_line, red, green, blue)
    print(total)
