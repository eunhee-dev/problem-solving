""" solve.py for 10804번. 카드 역배치 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(intervals: list[tuple[int, int]]) -> list[int]:
    cards = list(range(1, 21))
    for a, b in intervals:
        cards[a - 1:b] = cards[a - 1:b][::-1]
    return cards


def main() -> None:
    intervals = [(a, b) for a, b in (map(int, sys_input().split()) for _ in range(10))]

    result: list[int] = solve(intervals)
    print(*result)


if __name__ == "__main__":
    main()
