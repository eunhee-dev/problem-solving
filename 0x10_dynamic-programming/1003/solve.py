""" solve.py for 1003번. 피보나치 함수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> tuple[int, int]:
    if n == 0:
        return 1, 0

    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][0] = 1
    dp[1][1] = 1

    for i in range(2, n + 1):
        dp[0][i] = dp[0][i - 1] + dp[0][i - 2]
        dp[1][i] = dp[1][i - 1] + dp[1][i - 2]

    return dp[0][n], dp[1][n]


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        n = int(sys_input())

        answer: tuple[int, int] = solve(n)
        print(*answer, sep=" ")


if __name__ == "__main__":
    main()
