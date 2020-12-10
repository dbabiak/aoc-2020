from typing import List
from collections import defaultdict


S1 = '''\
16
10
15
5
1
11
7
19
6
12
4
'''

S2 = '''\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''

def d10p1(xs: List[int]) -> int:
    counts = defaultdict(int, {3: 1})
    acc = 0
    for i, x in enumerate(xs):
        jump = x - acc
        assert 1 <= jump <= 3

        counts[jump] += 1
        acc = x
    return counts[1] * counts[3]


def d10p2(xs: List[int]) -> int:
    memo = defaultdict(int, {0: 1})
    for i, x in enumerate(xs + [max(xs) + 3]):
        memo[x] = memo[x - 3] + memo[x - 2] + memo[x - 1]
    return max(memo.values())


def main():
    # xs = sorted(int(x) for x in S2.splitlines())
    with open('data/d10.txt') as fp:
        xs = sorted(int(x) for x in fp)
    print('p1', d10p1(xs))
    print('p2', d10p2(xs))


if __name__ == '__main__':
    main()
