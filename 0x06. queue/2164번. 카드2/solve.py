""" solve.py for 2164번. 카드2 """

from collections import deque


def main(n: int) -> None:
    cards = deque(range(1, n+1))

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())

    return cards[0]


if __name__ == "__main__":
    input_n = int(input())

    answer: int = main(input_n)
    print(answer)
