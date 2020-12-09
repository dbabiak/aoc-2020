from typing import List, Set, Callable


def make_bizarro_cdf(xs: List[int]) -> Callable[[int], int]:
    F_xs = [xs[0]]
    for i, x in enumerate(xs):
        if i == 0:
            continue
        F_xs.append(F_xs[-1] + x)

    def F(i):
        # F(i) returns sum(x for j, x in enumerate(xs) if j <= i)
        return F_xs[i]

    return F


def is_sum_of_two(target: int, lo: int, hi: int, xs: List[int]) -> bool:
    # i really want "inclusive-range"
    for i in range(lo, hi):
        for j in range(lo + 1, hi + 1):
            if xs[i] + xs[j] == target:
                return True
    return False


def d9p1(xs: List[int], prefix_length: int) -> int:
    for i, x in enumerate(xs):
        if i < prefix_length:
            continue

        if not is_sum_of_two(target=x, lo=i-prefix_length, hi=i-1, xs=xs):
            return x


def d9p2(xs: List[int], target: int) -> int:
    F = make_bizarro_cdf(xs)
    lo = 0
    hi = 0
    while True:
        acc = F(hi) - F(lo) + xs[lo]
        if acc == target:
            return min(xs[lo:hi+1]) + max(xs[lo:hi+1])
        elif acc < target:
            hi += 1
        elif acc > target:
            lo += 1


def main():
    with open('data/d09.txt') as fp:
        xs = [int(x) for x in fp]

    print('d9p1', d9p1(xs, prefix_length=25))
    print('d9p2', d9p2(xs, 23278925))


if __name__ == '__main__':
    main()
