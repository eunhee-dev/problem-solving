""" solve_precomputed.py for 15686번. 치킨 배달 """

import sys
from itertools import combinations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int, board: list[list[int]]) -> int:
    houses = []
    chicken_stores = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                houses.append((x, y))
            elif board[x][y] == 2:
                chicken_stores.append((x, y))

    # dist_matrix[i][j] : i번째 치킨집에서 j번째 집까지 치킨 거리
    dist_matrix = [[abs(cx - hx) + abs(cy - hy) for hx, hy in houses] for cx, cy in chicken_stores]
    min_dist = float("inf")

    for store_idx_comb in combinations(range(len(chicken_stores)), m):
        house_mins = [float("inf")] * len(houses)  # 각 집까지의 현재 선택된 치킨집 중 최단 거리
        for s_idx in store_idx_comb:
            for h_idx, _ in enumerate(houses):
                if house_mins[h_idx] > dist_matrix[s_idx][h_idx]:
                    house_mins[h_idx] = dist_matrix[s_idx][h_idx]
        min_dist = min(min_dist, sum(house_mins))

    return min_dist


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
