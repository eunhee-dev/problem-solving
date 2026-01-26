""" solve.py for 11931번. 수 정렬하기 4 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(nums: list[int]) -> list[int]:
    return list(sorted(nums, reverse=True))


def main() -> None:
    n = int(sys_input())
    nums = [int(sys.stdin.readline()) for _ in range(n)]

    answer: list[int] = solve(nums)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
