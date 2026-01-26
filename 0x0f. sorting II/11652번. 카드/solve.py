""" solve.py for 11652번. 카드 """

import sys
from collections import Counter


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(cards: list[int]) -> int:
    cards.sort()
    count = Counter(cards)
    return count.most_common(1)[0][0]


def main() -> None:
    n = int(sys_input())
    cards = [int(sys_input()) for _ in range(n)]

    answer: int = solve(cards)
    print(answer)


if __name__ == "__main__":
    main()
