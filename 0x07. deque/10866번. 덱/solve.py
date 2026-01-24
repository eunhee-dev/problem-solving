""" solve.py for 10866번. 덱 """ 

import sys
from collections import deque


def solve(n: int) -> None:
    sys_input = sys.stdin.readline
    my_deque = deque([])

    for _ in range(n):
        cmd = sys_input().rstrip().split()
        op = cmd[0]

        if op == "push_front":
            my_deque.appendleft(cmd[1])

        elif op == "push_back":
            my_deque.append(cmd[1])

        elif op == "pop_front":
            print(my_deque.popleft() if my_deque else -1)

        elif op == "pop_back":
            print(my_deque.pop() if my_deque else -1)

        elif op == "size":
            print(len(my_deque))

        elif op == "empty":
            print(0 if my_deque else 1)

        elif op == "front":
            print(my_deque[0] if my_deque else -1)

        elif op == "back":
            print(my_deque[-1] if my_deque else -1)

        else:
            raise ValueError()


if __name__ == "__main__":
    input_n = int(input())
    solve(input_n)
