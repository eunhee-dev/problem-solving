""" solve.py for 13300번. 방 배정 """

import sys
import math


MAX_GRADE = 6


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(k: int, students_info: list[tuple[int, int]]) -> int:
    student_cnts = [[0, 0] for _ in range(MAX_GRADE)]

    for s, y in students_info:
        student_cnts[y-1][s] += 1

    return sum(math.ceil(cnt / k) for grade in student_cnts for cnt in grade)


def main() -> None:
    n, k = map(int, sys_input().split())
    students_info = [tuple(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(k, students_info)
    print(answer)


if __name__ == "__main__":
    main()
