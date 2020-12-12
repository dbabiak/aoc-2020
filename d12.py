from typing import *

stub = """\
F10
N3
F7
R90
F11
"""

DIRECTIONS = dict(
    N=(0, 1),
    E=(1, 0),
    S=(0, -1),
    W=(-1, 0),
)


def manhattan(p1, p2) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def rotate_left(p):
    # (1,1) -> (-1,1), (-1,-1), (1,-1)
    x, y = p
    return -y, x


def rotate_right(p):
    # (1,1) -> (1,-1), (-1,-1), (-1,1)
    x, y = p
    return y, -x


def d12p1(xs: List[Tuple[str, int]]) -> int:
    x, y = 0, 0
    current_direction = (1, 0)
    for _dir, n in xs:
        if _dir in 'NESW':
            dx, dy = DIRECTIONS[_dir]
            x += n * dx
            y += n * dy
        elif _dir == 'L':
            for _ in range(int(n / 90)):
                current_direction = rotate_left(current_direction)
        elif _dir == 'R':
            for _ in range(int(n / 90)):
                current_direction = rotate_right(current_direction)
        elif _dir == 'F':
            dx, dy = current_direction
            x += n * dx
            y += n * dy
        else:
            assert False, "o_o"
    return manhattan((x, y), (0, 0))


def d12p2(xs: List[Tuple[str, int]]) -> int:
    x, y = 0, 0
    w_x, w_y = 10, 1
    for _dir, n in xs:
        if _dir in DIRECTIONS:
            dx, dy = DIRECTIONS[_dir]
            w_x += n * dx
            w_y += n * dy
        elif _dir == 'L':
            for _ in range(int(n / 90)):
                w_x, w_y = rotate_left((w_x, w_y))
        elif _dir == 'R':
            for _ in range(int(n / 90)):
                w_x, w_y = rotate_right((w_x, w_y))
        elif _dir == 'F':
            x += n * w_x
            y += n * w_y
        else:
            assert False, "o_o"
    return manhattan((x, y), (0, 0))


def main():
    # lines = stub.splitlines()
    # xs = [(line[0], int(line[1:])) for line in lines]
    with open('data/d12.txt') as fp:
        xs = [(line[0], int(line[1:])) for line in fp]
    print('d12p1', d12p1(xs))
    print('d12p2', d12p2(xs))


if __name__ == '__main__':
    main()
