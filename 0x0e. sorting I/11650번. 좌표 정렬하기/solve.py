""" solve.py for 11650번. 좌표 정렬하기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(coords: list[tuple[int, int]]) -> list[str]:
    return [f"{x} {y}" for x, y in sorted(coords)]


def main() -> None:
    n = int(sys_input())
    coords = [tuple(map(int, sys_input().split())) for _ in range(n)]

    answer: list[str] = solve(coords)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
