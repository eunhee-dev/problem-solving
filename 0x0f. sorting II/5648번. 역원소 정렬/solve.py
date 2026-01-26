""" solve.py for 5648번. 역원소 정렬 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(nums: list[str]) -> list[int]:
    new_nums = [0] * len(nums)
    for i, num_str in enumerate(nums):
        new_nums[i] = int(num_str[::-1])
    new_nums.sort()
    return new_nums


def main() -> None:
    first_line = sys_input().split()
    n, nums = int(first_line[0]), first_line[1:]
    while len(nums) < n:
        nums.extend(sys_input().split())

    answer: list[int] = solve(nums)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
