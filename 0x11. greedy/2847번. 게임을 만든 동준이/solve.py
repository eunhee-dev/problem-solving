""" solve.py for 2847번. 게임을 만든 동준이 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(points: list[int]) -> int:
    total = 0
    prev_point = points[-1]

    for curr_point in reversed(points[:-1]):
        if curr_point >= prev_point:
            total += curr_point - (prev_point - 1)
            curr_point = prev_point - 1
        prev_point = curr_point

    return total


def main() -> None:
    n = int(sys_input())
    points = [int(sys_input()) for _ in range(n)]

    answer: int = solve(points)
    print(answer)


if __name__ == "__main__":
    main()
