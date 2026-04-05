""" solve_naive_backtrack.py for 15684번. 사다리 조작 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def check(n: int, h: int, has_horizontal: list[list[int]]) -> bool:
    for i in range(n):
        curr_i = i
        for x in range(h):
            curr_i += has_horizontal[x][curr_i]
        if i != curr_i:
            return False
    return True


def solve(n: int, h: int, horizontals: list[tuple[int, int]]) -> int:
    min_count = float("inf")

    has_horizontal = [[0] * n for _ in range(h)]
    for x, y in horizontals:
        has_horizontal[x - 1][y - 1] = 1
        has_horizontal[x - 1][y] = -1

    def backtrack(start: int, depth: int) -> None:
        nonlocal min_count
        if check(n, h, has_horizontal):
            min_count = min(min_count, depth)
            return

        if depth == 3:
            return

        for curr in range(start, (n - 1) * h):
            x, y = divmod(curr, n - 1)
            if has_horizontal[x][y] or has_horizontal[x][y + 1]:
                continue

            has_horizontal[x][y] = 1
            has_horizontal[x][y + 1] = -1
            backtrack(curr + 1, depth + 1)
            has_horizontal[x][y] = 0
            has_horizontal[x][y + 1] = 0

    backtrack(0, 0)
    return min_count if min_count != float("inf") else -1


def main() -> None:
    n, m, h = map(int, sys_input().split())
    horizontals = [tuple(map(int, sys_input().split())) for _ in range(m)]

    answer: int = solve(n, h, horizontals)
    print(answer)


if __name__ == "__main__":
    main()
