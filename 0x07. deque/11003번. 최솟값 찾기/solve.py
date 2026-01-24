""" solve.py for 11003번. 최솟값 찾기 """ 

import sys
from collections import deque


def solve(l: int, a: list) -> str:
    deq = deque()
    min_list = []

    for i, num in enumerate(a):
        while deq and a[deq[-1]] > num:
            deq.pop()
        deq.append(i)

        if deq[0] <= i - l:
            deq.popleft()

        min_list.append(str(a[deq[0]]))

    return " ".join(min_list)


if __name__ == "__main__":
    sys_input = sys.stdin.readline

    _, input_l = map(int, input().split())
    input_a = list(map(int, sys_input().rstrip().split()))

    answer: str = solve(input_l, input_a)
    sys.stdout.write(answer)
