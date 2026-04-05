""" solve_itertools.py for 15684번. 사다리 조작 """

import sys
from itertools import combinations


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
    has_horizontal = [[0] * n for _ in range(h)]
    for x, y in horizontals:
        has_horizontal[x - 1][y - 1] = 1
        has_horizontal[x - 1][y] = -1

    candidates = [(x, y) for x in range(h) for y in range(n - 1)
                  if has_horizontal[x][y] == 0 and has_horizontal[x][y + 1] == 0]

    for count in range(4):
        for cand_comb in combinations(candidates, count):
            # --- 가지치기 ---
            is_valid_comb = True
            for cand1, cand2 in zip(cand_comb, cand_comb[1:]):
                if cand1[0] == cand2[0] and cand2[1] - cand1[1] == 1:
                    is_valid_comb = False
                    break
            if not is_valid_comb:
                continue
            # ---------------

            for x, y in cand_comb:
                has_horizontal[x][y] = 1
                has_horizontal[x][y + 1] = -1

            if check(n, h, has_horizontal):
                return count

            for x, y in cand_comb:
                has_horizontal[x][y] = 0
                has_horizontal[x][y + 1] = 0
    return -1


def main() -> None:
    n, m, h = map(int, sys_input().split())
    horizontals = [tuple(map(int, sys_input().split())) for _ in range(m)]

    answer: int = solve(n, h, horizontals)
    print(answer)


if __name__ == "__main__":
    main()
