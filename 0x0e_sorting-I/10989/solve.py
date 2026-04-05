""" solve.py for 10989번. 수 정렬하기 3 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[int]:
    counts = [0] * 10001
    for _ in range(n):
        num = int(sys_input())
        counts[num] += 1

    return counts


def main() -> None:
    n = int(sys_input())

    answer: list[int] = solve(n)
    for i in range(10001):
        for _ in range(answer[i]):
            print(i)


if __name__ == "__main__":
    main()
