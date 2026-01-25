""" solve.py for 14889번. 스타트와 링크 """

import sys
from itertools import combinations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, s: list[list[int]]) -> int:
    min_abil_diff = float("inf")
    members = list(range(n))

    for team1 in combinations(members, n // 2):
        team2 = list(set(members) - set(team1))

        team1_abil = 0
        team2_abil = 0

        for i, j in combinations(team1, 2):
            team1_abil += s[i][j] + s[j][i]

        for i, j in combinations(team2, 2):
            team2_abil += s[i][j] + s[j][i]

        min_abil_diff = min(min_abil_diff, abs(team1_abil - team2_abil))

    return min_abil_diff


def main() -> None:
    n = int(sys_input())
    s = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, s)
    print(answer)


if __name__ == "__main__":
    main()
