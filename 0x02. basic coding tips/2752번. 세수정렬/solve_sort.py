""" solve_sort.py for 2752번. 세수정렬 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int, c: int) -> list[int]:
    return sorted([a, b, c])


def main() -> None:
    a, b, c = map(int, sys_input().split())

    answer: list[int] = solve(a, b, c)
    print(*answer)


if __name__ == "__main__":
    main()
