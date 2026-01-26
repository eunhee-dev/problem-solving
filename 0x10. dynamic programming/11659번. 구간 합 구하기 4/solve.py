""" solve.py for 11659번. 구간 합 구하기 4 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, seq: list[int], intervals: list[tuple[int, int]]) -> list[int]:
    answer = []
    seq = [0] + seq
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + seq[i]

    for start, end in intervals:
        answer.append(dp[end] - dp[start - 1])

    return answer


def main() -> None:
    n, m = map(int, sys_input().split())
    seq = list(map(int, sys_input().split()))
    intervals = list((s, e) for s, e in (map(int, sys_input().split()) for _ in range(m)))

    answer: list[int] = solve(n, seq, intervals)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
