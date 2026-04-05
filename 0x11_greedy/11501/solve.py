""" solve.py for 11501번. 주식 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(prices: list[int]) -> int:
    total = 0
    max_price = prices[-1]

    for price in reversed(prices[:-1]):
        if price >= max_price:
            max_price = price
        else:
            total += max_price - price

    return total


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        _ = int(sys_input())
        prices = list(map(int, sys_input().split()))

        answer: int = solve(prices)
        print(answer)


if __name__ == "__main__":
    main()
