""" solve.py for 11052번. 카드 구매하기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, p: list[int]) -> int:
    p = [0] + p
    dp = p[::]

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], dp[j] + dp[i - j])

    return dp[n]


def main() -> None:
    n = int(sys_input())
    p = list(map(int, sys_input().split()))

    answer: int = solve(n, p)
    print(answer)


if __name__ == "__main__":
    main()
