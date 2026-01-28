""" solve.py for 2309. 일곱 난쟁이 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(heights: list[int]) -> list[int]:
    total = sum(heights)
    target = total - 100  # 제외할 2명의 키 합
    n = len(heights)

    for i in range(n):
        for j in range(i + 1, n):
            if heights[i] + heights[j] == target:
                return sorted(h for h in heights if h not in (heights[i], heights[j]))

    return []


def main() -> None:
    heights = [int(sys_input()) for _ in range(9)]

    result: list[int] = solve(heights)
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
