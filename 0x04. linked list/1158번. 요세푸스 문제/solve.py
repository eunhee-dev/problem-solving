""" solve.py for 1158번. 요세푸스 문제 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, k: int) -> str:
    removed = []
    people = deque(range(1, n+1))
    while people:
        people.rotate(-(k-1))
        removed.append(str(people.popleft()))

    return "<" + ", ".join(removed) + ">"


def main() -> None:
    n, k = map(int, sys_input().split())

    answer: str = solve(n, k)
    print(answer)


if __name__ == "__main__":
    main()
