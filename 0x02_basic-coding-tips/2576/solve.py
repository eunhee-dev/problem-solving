""" solve.py for 2576번. 홀수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(nums: list[int]) -> list[int]:
    odds = [n for n in nums if n % 2 == 1]
    if not odds:
        return [-1]
    return [sum(odds), min(odds)]


def main() -> None:
    nums = [int(sys_input()) for _ in range(7)]

    answer: list[int] = solve(nums)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
