""" solve.py for 1912번. 연속합 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, seq: list[int]) -> int:
    dp = [float("-inf")] * (n + 1)
    seq = [0] + seq

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + seq[i] if dp[i - 1] > 0 else seq[i]

    return max(dp)


def main() -> None:
    n = int(sys_input())
    seq = list(map(int, sys_input().split()))

    answer: int = solve(n, seq)
    print(answer)


if __name__ == "__main__":
    main()
