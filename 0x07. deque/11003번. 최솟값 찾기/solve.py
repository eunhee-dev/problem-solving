""" solve.py for 11003번. 최솟값 찾기 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(l: int, a: list[int]) -> list[int]:
    deq = deque()
    min_list = []

    for i, num in enumerate(a):
        while deq and a[deq[-1]] > num:
            deq.pop()
        deq.append(i)

        if deq[0] <= i - l:
            deq.popleft()

        min_list.append(a[deq[0]])

    return min_list


def main() -> None:
    _, l = map(int, sys_input().split())
    a = list(map(int, sys_input().split()))

    answer: list[int] = solve(l, a)
    sys.stdout.write(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()
