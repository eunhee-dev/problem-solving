""" solve.py for 10093번. 숫자 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int) -> tuple[int, list[int]]:
    lo, hi = min(a, b), max(a, b)
    between = list(range(lo + 1, hi))
    return len(between), between


def main() -> None:
    a, b = map(int, sys_input().split())

    answer: tuple[int, list[int]] = solve(a, b)
    print(answer[0])
    print(*answer[1])


if __name__ == "__main__":
    main()
