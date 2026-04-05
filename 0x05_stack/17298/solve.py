""" solve.py for 17298번. 오큰수"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, nums: list[int]) -> list[int]:
    res = [-1] * n
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            prev_idx = stack.pop()
            res[prev_idx] = num
        stack.append(i)
    return res


def main() -> None:
    n = int(sys_input())
    nums = list(map(int, sys_input().split()))

    answer: list[int] = solve(n, nums)
    print(*answer)


if __name__ == "__main__":
    main()
