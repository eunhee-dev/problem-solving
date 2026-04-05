""" solve.py for 6198번. 옥상 정원 꾸미기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, heights: list[int]) -> int:
    stack = []
    visible_count = 0

    for idx, height in enumerate(heights):
        while stack and heights[stack[-1]] <= height:
            prev_idx = stack.pop()
            visible_count += idx - prev_idx - 1
        stack.append(idx)

    for remaining_idx in stack:
        visible_count += n - remaining_idx - 1

    return visible_count


def main() -> None:
    n = int(sys_input())
    heights = [int(sys_input()) for _ in range(n)]

    answer: int = solve(n, heights)
    print(answer)


if __name__ == "__main__":
    main()
