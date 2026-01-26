""" solve.py for 11053번. 가장 긴 증가하는 부분 수열 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, a: list[int]) -> int:
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main() -> None:
    n = int(sys_input())
    a = list(map(int, sys_input().split()))

    answer: int = solve(n, a)
    print(answer)


if __name__ == "__main__":
    main()
