""" solve.py for 7570번. 줄 세우기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, childrens: list[int]) -> int:
    dp = [0] * (n + 1)

    for v in childrens:
        dp[v] = dp[v - 1] + 1

    return n - max(dp)


def main() -> None:
    n = int(sys_input())
    childrens = list(map(int, sys_input().split()))

    answer: int = solve(n, childrens)
    print(answer)


if __name__ == "__main__":
    main()
