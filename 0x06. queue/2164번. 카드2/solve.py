""" solve.py for 2164번. 카드2 """

from collections import deque


def solve(n: int) -> int:
    cards = deque(range(1, n + 1))

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())

    return cards[0]


def main() -> None:
    n = int(input())

    result: int = solve(n)
    print(result)


if __name__ == "__main__":
    main()
