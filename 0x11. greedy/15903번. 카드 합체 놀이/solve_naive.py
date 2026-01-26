""" solve_naive.py for 15903번. 카드 합체 놀이 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(m: int, cards: list[int]) -> int:
    for _ in range(m):
        cards.sort(reverse=True)
        x = cards.pop()
        y = cards.pop()
        for _ in range(2):
            cards.append(x + y)

    return sum(cards)


def main() -> None:
    _, m = map(int, sys_input().split())
    cards = list(map(int, sys_input().split()))

    answer: int = solve(m, cards)
    print(answer)


if __name__ == "__main__":
    main()
