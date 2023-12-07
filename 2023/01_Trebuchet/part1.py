import re


def find_value(line):
    regex_first = re.compile(r'\D*(\d).*')
    regex_last = re.compile(r'.*(\d)\D*')

    first = regex_first.match(line).group(1)
    last = regex_last.match(line).group(1)

    return int(first + last)


if __name__ == '__main__':
    total = 0
    with open('input.txt') as file:
        for s_line in file:
            total += find_value(s_line)
    print(total)
