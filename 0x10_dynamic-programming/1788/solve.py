""" solve.py for 1788번. 피보나치 수의 확장 """

import sys


MOD = 1_000_000_000


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> tuple[int, int]:
    if n == 0:
        return 0, 0

    abs_n = abs(n)

    dp = [0] * (abs_n + 1)
    dp[1] = 1

    for i in range(2, abs_n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % MOD

    if n < 0 and n % 2 == 0:
        return -1, dp[abs_n]

    return 1, dp[abs_n]


def main() -> None:
    n = int(sys_input())

    answer: tuple[int, int] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
