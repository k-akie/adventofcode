import re


def solve(_line: str) -> int:
    result = re.compile(r'Game (\d+): (.*)').match(_line).groups()
    cubes = re.split('[,;]', result[1])

    bag = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    regex = re.compile(r'\s?(\d+) (.*)')
    for cube in cubes:
        s_num,  name = regex.match(cube).groups()
        num = int(s_num)

        if bag[name] < num:
            bag[name] = num

    power = 1
    for value in bag.values():
        power *= value
    return power


if __name__ == '__main__':
    total = 0
    with open('input.txt') as file:
        for s_line in file:
            total += solve(s_line)
    print(total)
