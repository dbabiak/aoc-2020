import os
from typing import Iterable
import time

S = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''

DELTAS = (
     (-1,-1),
     (0,-1),
     (1,-1),

     (-1, 0),
     (1, 0),

     (-1, 1),
     (0, 1),
     (1, 1),
)

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def in_bounds(grid, pos) -> bool:
    if len(grid) == 0 or len(grid[0]) == 0:
        return False

    row, col = pos
    return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))


def nbrs(grid, pos) -> Iterable[str]:
    row, col = pos
    return (
        grid[row + dr][col + dc]
        for dr, dc in DELTAS
        if in_bounds(grid, (row + dr, col + dc))
    )


def do_step(grid) -> bool:
    on = []
    off = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):

            if cell == FLOOR:
                continue

            n_occupied = sum(1 for x in nbrs(grid, (r, c)) if x == OCCUPIED)

            if cell == EMPTY and n_occupied == 0:
                on.append((r, c))

            if cell == OCCUPIED and n_occupied >= 4:
                off.append((r,c))

    for row, col in on:
        grid[row][col] = OCCUPIED

    for row, col in off:
        grid[row][col] = EMPTY

    return (not on) and (not off)


def d11p1(grid) -> int:
    i = 0
    def print_grid():
        print(i)
        for l in grid:
            print(' '.join(l))

    while True:
        os.system('clear')
        print_grid()
        time.sleep(0.3)
        should_stop = do_step(grid)
        i += 1
        if should_stop:
            break
    return sum(1 for row in grid for _, cell in enumerate(row) if cell == OCCUPIED)


def d11p2(grid) -> int:
    i = 0
    def print_grid():
        print(i)
        for l in grid:
            print(' '.join(l))

    while True:
        os.system('clear')
        print_grid()
        time.sleep(0.2)
        should_stop = do_step_p2(grid)
        if should_stop:
            break
    return sum(1 for row in grid for _, cell in enumerate(row) if cell == OCCUPIED)


def first_seat_in_direction(grid, r_c, dr_dc):
    r, c = r_c
    dr, dc = dr_dc
    cell = FLOOR

    while True:
        r += dr
        c += dc
        if not in_bounds(grid, (r,c)):
            return cell
        cell = grid[r][c]

        if cell != FLOOR:
            return cell


def do_step_p2(grid) -> bool:
    on = []
    off = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):

            if cell == FLOOR:
                continue

            nbrs = [first_seat_in_direction(grid, (r,c), delta) for delta in DELTAS]
            n_occupied = sum(1 for x in nbrs if x == OCCUPIED)

            if cell == EMPTY and n_occupied == 0:
                on.append((r, c))

            if cell == OCCUPIED and n_occupied >= 5:
                off.append((r,c))

    for row, col in on:
        grid[row][col] = OCCUPIED

    for row, col in off:
        grid[row][col] = EMPTY

    return (not on) and (not off)


def main():
    # grid = [list(*line.strip().split()) for line in S.splitlines()]

    with open('data/d11.txt') as fp:
        grid = [list(*line.strip().split()) for line in fp]

    for i, l in enumerate(grid):
        print(i, l)
    print('\n--------------------------\n')
    # print(d11p1(grid))
    print(d11p2(grid))


if __name__ == '__main__':
    main()
