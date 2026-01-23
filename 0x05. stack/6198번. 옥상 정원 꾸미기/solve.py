# solve.py for 6198번. 옥상 정원 꾸미기
import sys


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


if __name__ == "__main__":
    sys_input = sys.stdin.readline

    input_n = int(input())
    input_heights = [int(sys_input().rstrip()) for _ in range(input_n)]

    answer: int = solve(input_n, input_heights)
    print(answer)
