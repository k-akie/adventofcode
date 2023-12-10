import re


def pre(_line: str) -> [int]:
    r = re.compile(r'[^.0-9]')

    result = []
    for i in range(len(_line)):
        if r.match(_line[i]):
            result.append(i)

    return result


def solve(_num: int, _line: str, _symbols: [[int]]) -> int:
    p = r'\D*(\d*)'
    matched = re.compile(f"\\D*(\\d+){p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}").match(_line)
    if not matched:
        return 0

    part_sum = 0
    added = set()

    #  0行
    symbol = _symbols[_num]
    for g in range(1, len(matched.groups())):
        s = matched.start(g)
        e = matched.end(g)
        for p in symbol:
            if s <= p <= e:
                if matched.group(g) and (g not in added):
                    added.add(g)
                    part_sum += int(matched.group(g))

    # -1行
    if _num > 0:
        symbol = _symbols[_num - 1]
        for g in range(1, len(matched.groups())):
            s = matched.start(g) - 1
            e = matched.end(g) + 1
            for p in symbol:
                if s <= p <= e:
                    if matched.group(g) and (g not in added):
                        added.add(g)
                        part_sum += int(matched.group(g))

    # +1行
    if _num < len(_symbols) - 1:
        symbol = _symbols[_num + 1]
        for g in range(1, len(matched.groups())):
            s = matched.start(g) - 1
            e = matched.end(g) + 1
            for p in symbol:
                if s <= p <= e:
                    if matched.group(g) and (g not in added):
                        added.add(g)
                        part_sum += int(matched.group(g))

    return part_sum


if __name__ == '__main__':
    texts = []
    symbols = [[]]
    with open('input.txt') as file:
        for s_line in file:
            texts.append(s_line)
            symbols.append(pre(s_line))

    total = 0
    for i in range(len(texts)):
        total += solve(i, texts[i], symbols)

    print(total)
