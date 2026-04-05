""" solve_counter.py for 2480. 주사위 세개 """

import sys
from collections import Counter


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(dice: list[int]) -> int:
    counter = Counter(dice)
    value, count = counter.most_common(1)[0]

    if count == 3:
        return 10000 + value * 1000
    if count == 2:
        return 1000 + value * 100
    return max(dice) * 100


def main() -> None:
    dice = list(map(int, sys_input().split()))

    answer: int = solve(dice)
    print(answer)


if __name__ == "__main__":
    main()
