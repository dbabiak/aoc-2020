import sys
from collections import defaultdict, deque
import re
from typing import Dict, List, Tuple, Optional
from pprint import pprint

input = """\
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
            m[color].append((n, c))
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
    pprint(seen)
    return len(seen)


def main() -> None:
    with open('data/d07.txt') as fp:
        lines = [line.strip() for line in fp]

    rules = parse_rules(lines)
    pprint(rules)
    print()
    pprint(invert_map(rules))
    print('d7p1', d7p1(invert_map(rules)))
    print(rules['shiny gold'])



if __name__ == '__main__':
    main()

