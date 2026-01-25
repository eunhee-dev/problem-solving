""" solve.py for 14956번. Philosopher’s Walk """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


BASE_COORD = [(1, 1), (1, 2), (2, 2), (2, 1)]


def solve(n: int, m: int) -> tuple[int, int]:
    if n == 2:
        return BASE_COORD[m]

    prev_n = n // 2
    quadrant, remain = divmod(m, prev_n ** 2)
    x, y = solve(prev_n, remain)

    if quadrant == 0:
        x, y = y, x
    elif quadrant == 3:
        x, y = prev_n - y + 1, prev_n - x + 1

    shift = {
        0: (0, 0),
        1: (0, prev_n),
        2: (prev_n, prev_n),
        3: (prev_n, 0)
    }

    dx, dy = shift[quadrant]
    return (x + dx, y + dy)


def main() -> None:
    n, m = map(int, sys_input().split())

    answer: tuple[int, int] = solve(n, m-1)  # 1-based => 0-based
    print(*answer)


if __name__ == "__main__":
    main()
