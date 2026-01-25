""" solve.py for 15686번. 치킨 배달 """

import sys
from itertools import combinations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_chicken_dist(house: tuple[int, int], store_comb: list[tuple[int, int]]) -> int:
    return min(abs(house[0] - store[0]) + abs(house[1] - store[1]) for store in store_comb)


def solve(n: int, m: int, board: list[list[int]]) -> int:
    houses = []
    chicken_stores = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                houses.append((x, y))
            elif board[x][y] == 2:
                chicken_stores.append((x, y))

    min_dist = float("inf")
    for store_comb in combinations(chicken_stores, m):
        city_chicken_dist = sum(get_chicken_dist(house, store_comb) for house in houses)
        min_dist = min(min_dist, city_chicken_dist)
    return min_dist


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
