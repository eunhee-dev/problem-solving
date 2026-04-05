""" solve.py for 2752번. 세수정렬 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int, c: int) -> tuple[int ,int, int]:
    max_num, min_num = max(a, b, c), min(a, b, c)
    return min_num, sum([a, b, c]) - max_num - min_num, max_num


def main() -> None:
    a, b, c = map(int, sys_input().split())

    answer: tuple[int, int, int] = solve(a, b, c)
    print(*answer)


if __name__ == "__main__":
    main()
