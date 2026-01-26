""" solve.py for 10814번. 나이순 정렬 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(members: list[list[str]]) -> list[str]:
    members.sort(key=lambda x: int(x[0]))
    return [" ".join(info) for info in members]


def main() -> None:
    n = int(sys_input())
    members = [sys_input().split() for _ in range(n)]

    answer: list[str] = solve(members)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
