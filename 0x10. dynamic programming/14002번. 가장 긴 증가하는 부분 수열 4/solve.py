""" solve.py for 14002번. 가장 긴 증가하는 부분 수열 4 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, a: list[int]) -> tuple[int, list[int]]:
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    curr, max_len = max(enumerate(dp), key=lambda x: x[1])
    path = []
    while curr != -1:
        path.append(a[curr])
        curr = prev[curr]

    return max_len, path[::-1]


def main() -> None:
    n = int(sys_input())
    a = list(map(int, sys_input().split()))

    answer: tuple[int, list[int]] = solve(n, a)
    print(answer[0])
    print(*answer[1], sep=" ")


if __name__ == "__main__":
    main()
