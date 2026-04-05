""" solve.py for 2750번. 수 정렬하기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(arr: list[int]) -> list[int]:
    return sorted(arr)


def main() -> None:
    n = int(sys_input())
    arr = list(int(sys_input()) for _ in range(n))

    answer: list[int] = solve(arr)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
