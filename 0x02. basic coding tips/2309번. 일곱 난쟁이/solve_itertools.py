""" solve_itertools.py for 2309번. 일곱 난쟁이 """

import sys
from itertools import combinations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(heights: list[int]) -> list[int]:
    total = sum(heights)
    target = total - 100  # 제외할 2명의 키 합

    for a, b in combinations(heights, 2):
        if a + b == target:
            return sorted(h for h in heights if h not in (a, b))

    return []


def main() -> None:
    heights = [int(sys_input()) for _ in range(9)]

    answer: list[int] = solve(heights)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
