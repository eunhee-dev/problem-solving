""" solve.py for 2302번. 극장 좌석 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, vip: set[int]) -> int:
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        if i in vip or i - 1 in vip:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main() -> None:
    n = int(sys_input())
    m = int(sys_input())
    vip = {int(sys_input()) for _ in range(m)}

    answer: int = solve(n, vip)
    print(answer)


if __name__ == "__main__":
    main()
