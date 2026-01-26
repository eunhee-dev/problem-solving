""" solve.py for 9095번. 1, 2, 3 더하기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    dp = [0] * 11
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


def main() -> None:
    t = int(sys_input())

    for _ in range(t):
        n = int(sys_input())

        answer: int = solve(n)
        print(answer)


if __name__ == "__main__":
    main()
