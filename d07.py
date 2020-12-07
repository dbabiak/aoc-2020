import re
from collections import defaultdict, deque
from typing import Dict, List, Tuple

S1 = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

S2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""


rgx = re.compile(r'(\d) ([a-zA-Z ]+) bag')


def invert_map(kv: Dict[str, List[Tuple[int, str]]]) -> Dict[str, List[str]]:
    vk = defaultdict(list)
    for k, n_vs in kv.items():
        for _, v in n_vs:
            vk[v].append(k)
    return dict(vk.items())


def parse_rules(lines: List[str]) -> Dict[str, List[Tuple[int, str]]]:
    m = {}
    for line in lines:
        x, y = line.split('contain')
        y = y.rstrip('.')
        zs = y.split(',')
        color = x[:-len(' bags')].strip()
        m[color] = []
        for z in zs:
            if z.strip().startswith('no other'):
                break
            [(n, c)] = rgx.findall(z)
            m[color].append((int(n), c))
    return m


def d7p1(inverse_map: Dict[str, List[str]], start: str = 'shiny gold') -> int:
    seen = set()
    q = deque([start])
    while q:
        node = q.popleft()
        for nbr in inverse_map.get(node, []):
            if nbr not in seen:
                seen.add(nbr)
                q.append(nbr)
    return len(seen)


def d7p2(rules: Dict[str, List[Tuple[int, str]]], start='shiny gold') -> int:
    memo = {}

    def _lookup(node: str) -> int:
        if node in memo:
            return memo[node]
        n = 1 + sum(k*_lookup(nbr) for k, nbr in rules[node])
        memo[node] = n
        return n

    return _lookup(start) - 1


def main() -> None:
    with open('data/d07.txt') as fp:
        lines = [line.strip() for line in fp]

    rules = parse_rules(lines)
    print('d7p1', d7p1(invert_map(rules)))
    print('d7p2', d7p2(rules))


if __name__ == '__main__':
    main()
