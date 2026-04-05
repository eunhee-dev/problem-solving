""" solve.py for 10825번. 국영수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(rows: list[list[str]]) -> list[str]:
    grade_info = [(row[0], int(row[1]), int(row[2]), int(row[3])) for row in rows]
    grade_info.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    return [row[0] for row in grade_info]


def main() -> None:
    n = int(sys_input())
    rows = [sys_input().split() for _ in range(n)]

    answer: list[str] = solve(rows)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
