""" solve.py for 15903번. 카드 합체 놀이 """

import sys
import heapq


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(m: int, cards: list[int]) -> int:
    heapq.heapify(cards)

    for _ in range(m):
        x = heapq.heappop(cards)
        y = heapq.heappop(cards)
        for _ in range(2):
            heapq.heappush(cards, x + y)

    return sum(cards)


def main() -> None:
    _, m = map(int, sys_input().split())
    cards = list(map(int, sys_input().split()))

    answer: int = solve(m, cards)
    print(answer)


if __name__ == "__main__":
    main()
