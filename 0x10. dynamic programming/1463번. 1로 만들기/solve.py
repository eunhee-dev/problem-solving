""" solve.py for 1463번. 1로 만들기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

    return dp[n]


def main() -> None:
    n = int(sys_input())

    answer: int = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
