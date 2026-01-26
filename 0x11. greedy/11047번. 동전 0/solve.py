""" solve.py for 11047번. 동전 0 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int, coins: list[int]) -> int:
    count = 0
    for i in range(len(coins) - 1, -1, -1):
        count += k // coins[i]
        k %= coins[i]
        if k == 0:
            break
    return count


def main() -> None:
    n, k = map(int, sys_input().split())
    coins = [int(sys_input()) for _ in range(n)]

    answer: int = solve(k, coins)
    print(answer)


if __name__ == "__main__":
    main()
