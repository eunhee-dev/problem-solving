""" solve.py for 2587번. 대표값2 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(nums: list[int]) -> tuple[int, int]:
    avg = sum(nums) // len(nums)
    median = sorted(nums)[len(nums) // 2]
    return avg, median


def main() -> None:
    nums = [int(sys_input()) for _ in range(5)]

    result: tuple[int, int] = solve(nums)
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
