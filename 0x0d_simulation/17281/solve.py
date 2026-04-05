""" solve.py for 17281번. ⚾ """

import sys
from itertools import permutations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def play(inning: list[int], order: tuple[int, ...], batter_idx: int) -> tuple[int, int]:
    inning_score = 0
    out_count = 0
    b1, b2, b3 = 0, 0, 0

    while out_count < 3:
        hit_result = inning[order[batter_idx]]

        if hit_result == 0:
            out_count += 1
        elif hit_result == 1:
            inning_score += b3
            b1, b2, b3 = 1, b1, b2
        elif hit_result == 2:
            inning_score += (b2 + b3)
            b1, b2, b3 = 0, 1, b1
        elif hit_result == 3:
            inning_score += (b1 + b2 + b3)
            b1, b2, b3 = 0, 0, 1
        else:
            inning_score += (b1 + b2 + b3 + 1)
            b1, b2, b3 = 0, 0, 0

        batter_idx = (batter_idx + 1) % 9

    return batter_idx, inning_score


def solve(innings: list[list[int]]) -> int:
    max_score = 0

    for perm in permutations(range(1, 9)):
        order = perm[:3] + (0, ) + perm[3:]
        score = 0
        batter_idx = 0

        for inning in innings:
            batter_idx, inning_score = play(inning, order, batter_idx)
            score += inning_score

        max_score = max(max_score, score)

    return max_score


def main() -> None:
    n = int(sys_input())
    innings = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(innings)
    print(answer)


if __name__ == "__main__":
    main()
