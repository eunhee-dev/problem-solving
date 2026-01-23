""" solve.py for 10845번. 큐 """

import sys
from collections import deque


def main(n: int) -> None:
    sys_input = sys.stdin.readline
    queue = deque([])

    for _ in range(n):
        cmd = sys_input().rstrip().split()
        op = cmd[0]

        if op == "push":
            queue.append(cmd[1])

        elif op == "pop":
            print(queue.popleft() if queue else -1)

        elif op == "size":
            print(len(queue))

        elif op == "empty":
            print(0 if queue else 1)

        elif op == "front":
            print(queue[0] if queue else -1)

        elif op == "back":
            print(queue[-1] if queue else -1)

        else:
            raise ValueError()


if __name__ == "__main__":
    input_n = int(input())
    main(input_n)
