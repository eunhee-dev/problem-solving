""" solve.py for 3015번. 오아시스 재결합 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


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


def main() -> None:
    n = int(sys_input())
    heights = [int(sys_input()) for _ in range(n)]

    answer: int = solve(heights)
    print(answer)


if __name__ == "__main__":
    main()
