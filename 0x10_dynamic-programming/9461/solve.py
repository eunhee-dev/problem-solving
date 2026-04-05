""" solve.py for 9461번. 파도반 수열 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n_list: list[int]) -> list[int]:
    n = max(n_list)
    dp = [0, 1, 1, 1, 2, 2]

    for i in range(6, n + 1):
        dp.append(dp[i - 5] + dp[i - 1])

    return [dp[i] for i in n_list]


def main() -> None:
    t = int(sys_input())
    n_list = [int(sys_input()) for _ in range(t)]

    answer: list[int] = solve(n_list)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
