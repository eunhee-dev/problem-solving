""" solve2.py for 2302번. 극장 좌석 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, vip: list[int]) -> int:
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n - len(vip) + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    ans = 1
    curr_idx = 0
    # vip.sort() // 오름차순으로 입력이 들어오는 것이 문제 조건 상 보장됨
    for v in vip:
        ans *= dp[v - curr_idx - 1]
        curr_idx = v

    ans *= dp[n - curr_idx]

    return ans


def main() -> None:
    n = int(sys_input())
    m = int(sys_input())
    vip = [int(sys_input()) for _ in range(m)]

    answer: int = solve(n, vip)
    print(answer)


if __name__ == "__main__":
    main()
