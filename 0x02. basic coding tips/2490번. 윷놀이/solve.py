""" solve.py for 2490번. 윷놀이 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(yuts: list[list[int]]) -> list[str]:
    return ["DCBAE"[sum(yut)] for yut in yuts]


def main() -> None:
    yuts = [list(map(int, sys_input().split())) for _ in range(3)]

    answer: list[str] = solve(yuts)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
