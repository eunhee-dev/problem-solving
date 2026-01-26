""" solve.py for 1026번. 보물 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: list[int], b: list[int]) -> int:
    a.sort(reverse=True)
    b.sort()
    return sum(x * y for x, y in zip(a, b))


def main() -> None:
    _ = int(sys_input())
    a = list(map(int, sys_input().split()))
    b = list(map(int, sys_input().split()))

    answer: int = solve(a, b)
    print(answer)


if __name__ == "__main__":
    main()
