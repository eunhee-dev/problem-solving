""" solve.py for 2562번. 최댓값 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(nums: list[int]) -> tuple[int, int]:
    max_val = max(nums)
    max_idx = nums.index(max_val) + 1
    return max_val, max_idx


def main() -> None:
    nums = [int(sys_input()) for _ in range(9)]

    answer: tuple[int, int] = solve(nums)
    print(answer[0])
    print(answer[1])


if __name__ == "__main__":
    main()
