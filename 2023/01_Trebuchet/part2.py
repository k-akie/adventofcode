import re

patten = '(one|two|three|four|five|six|seven|eight|nine)'
dic = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def sub_letter_first(line):
    matched = re.match(f'.*?{patten}.*', line)
    if not matched:
        return line

    letter = matched.group(1)
    return re.sub(letter, dic[letter], line)


def sub_letter_last(line):
    matched = re.match(f'.*{patten}.*?', line)
    if not matched:
        return line

    letter = matched.group(1)
    return re.sub(letter, dic[letter], line)


def find_first(line):
    line = sub_letter_first(line)
    regex_first = re.compile(r'\D*(\d).*')
    return regex_first.match(line).group(1)


def find_last(line):
    line = sub_letter_last(line)
    regex_last = re.compile(r'.*(\d)\D*')
    return regex_last.match(line).group(1)


if __name__ == '__main__':
    total = 0
    with open('input.txt') as file:
        for s_line in file:
            result = find_first(s_line) + find_last(s_line)
            total += int(result)
    print(total)
