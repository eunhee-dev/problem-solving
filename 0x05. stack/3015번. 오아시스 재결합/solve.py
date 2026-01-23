# solve.py for 3015번. 오아시스 재결합
import sys


def solve(heights: list[int]) -> int:
    stack = []
    total_pairs = 0

    for height in heights:
        count = 1

        while stack and stack[-1][0] <= height:
            prev_count = stack[-1][1]
            total_pairs += prev_count
            if stack[-1][0] == height:
                count = prev_count + 1
            stack.pop()

        if stack:
            total_pairs += 1

        stack.append((height, count))

    return total_pairs


if __name__ == "__main__":
    sys_input = sys.stdin.readline

    input_n = int(input())
    input_heights = [int(sys_input().rstrip()) for _ in range(input_n)]

    answer: int = solve(input_heights)
    print(answer)
