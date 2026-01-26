""" solve.py for 15988번. 1, 2, 3 더하기 3 """

import sys


MOD = 1_000_000_009


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n_list: list[int]) -> list[int]:
    max_n = max(n_list)

    if max_n <= 2:
        return n_list

    dp = [0] * (max_n + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, max_n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

    return [dp[n] for n in n_list]


def main() -> None:
    t = int(sys_input())
    n_list = [int(sys_input()) for _ in range(t)]

    answer: list[int] = solve(n_list)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
