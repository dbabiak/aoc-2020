import re
from typing import Tuple, List

Op = Tuple[str, int]


def d8p1(ops: List[Op]) -> Tuple[int, bool]:
    seen = set()
    acc = 0
    i = 0
    while i < len(ops):
        op, n = ops[i]

        if i in seen:
            return acc, False
        seen.add(i)

        if 'nop' == op:
            i += 1
        elif 'jmp' == op:
            i += n
        elif 'acc' == op:
            acc += n
            i += 1

    return acc, True


def d8p2(ops: List[Op]) -> int:
    def flip(i: int):
        op, n = ops[i]
        if 'nop' == op:
            ops[i] = 'jmp', n
        elif 'jmp' == op:
            ops[i] = 'nop', n

    for i, (op, _) in enumerate(ops):
        if op not in ('nop', 'jmp'):
            continue

        flip(i)
        acc, is_ok = d8p1(ops)
        flip(i)
        if is_ok:
            return acc


def main() -> None:
    ops = parse_operations()
    print(d8p1(ops))
    print(d8p2(ops))


def parse_operations():
    rgx = re.compile(r'^([a-z]+) ([+\-][0-9]+)$')
    with open('data/d08.txt') as fp:
        lines = list(map(str.strip, fp))
    ops = []
    for line in lines:
        [(op, n)] = rgx.findall(line)
        ops.append((op, int(n)))
    return ops


if __name__ == '__main__':
    main()
