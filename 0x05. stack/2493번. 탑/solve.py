""" solve.py for 2493번. 탑 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, heights: list[int]) -> str:
    stack = []
    receivers = ["0"] * n

    for idx in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] < heights[idx]:
            prev_idx = stack.pop()
            receivers[prev_idx] = str(idx + 1)
        stack.append(idx)

    return " ".join(receivers)


def main() -> None:
    n = int(input())
    heights = list(map(int, sys_input().split()))

    answer: str = solve(n, heights)
    print(answer)


if __name__ == "__main__":
    main()
