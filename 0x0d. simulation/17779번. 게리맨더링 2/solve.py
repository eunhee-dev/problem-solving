""" solve.py for 17779번. 게리맨더링 2 """

import sys
from itertools import product


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def calc_diff(n: int, a: list[list[int]], comb: tuple[int, int, int, int], total: int) -> int:
    x, y, d1, d2 = comb
    board = [[0] * n for _ in range(n)]

    for i in range(d1 + 1):
        board[x + i][y - i] = 5
        board[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        board[x + i][y + i] = 5
        board[x + d1 + i][y - d1 + i] = 5

    population = [0] * 5

    # 1번 선거구: 왼쪽 → 오른쪽 스캔
    for r in range(x + d1):
        for c in range(y + 1):
            if board[r][c]:
                break
            population[0] += a[r][c]

    # 2번 선거구: 오른쪽 → 왼쪽 스캔
    for r in range(x + d2 + 1):
        for c in range(n - 1, y, -1):
            if board[r][c]:
                break
            population[1] += a[r][c]

    # 3번 선거구: 왼쪽 → 오른쪽 스캔
    for r in range(x + d1, n):
        for c in range(y - d1 + d2):
            if board[r][c]:
                break
            population[2] += a[r][c]

    # 4번 선거구: 오른쪽 → 왼쪽 스캔
    for r in range(x + d2 + 1, n):
        for c in range(n - 1, y - d1 + d2 - 1, -1):
            if board[r][c]:
                break
            population[3] += a[r][c]

    # 5번 선거구: 전체 - 1~4 선거구
    population[4] = total - sum(population[:4])

    return max(population) - min(population)


def solve(n: int, a: list[list[int]]) -> int:
    min_diff = float("inf")
    total = sum(map(sum, a))
    for x, y in product(range(n), repeat=2):
        for d1, d2 in product(range(1, n), repeat=2):
            if not 0 <= x <= x + d1 + d2 <= n - 1:
                continue
            if not 0 <= y - d1 < y < y + d2 <= n - 1:
                continue
            min_diff = min(min_diff, calc_diff(n, a, (x, y, d1, d2), total))

    return min_diff


def main() -> None:
    n = int(sys_input())
    a = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, a)
    print(answer)


if __name__ == "__main__":
    main()
