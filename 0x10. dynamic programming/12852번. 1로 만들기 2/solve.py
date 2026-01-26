""" solve.py for 12852번. 1로 만들기 2 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> tuple[int, list[int]]:
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2

    path = []
    curr = n
    while curr != 1:
        path.append(curr)
        curr = prev[curr]
    path.append(1)

    return dp[n], path


def main() -> None:
    n = int(sys_input())

    answer: tuple[int, list[int]] = solve(n)
    print(answer[0])
    print(*answer[1], sep=" ")


if __name__ == "__main__":
    main()
