""" solve.py for 18258번. 큐 2 """

import sys
from collections import deque


def main(n: int) -> None:
    sys_input = sys.stdin.readline
    queue = deque([])
    output = []

    for _ in range(n):
        cmd = sys_input().rstrip().split()
        op = cmd[0]

        if op == "push":
            queue.append(cmd[1])

        elif op == "pop":
            output.append(queue.popleft() if queue else "-1")

        elif op == "size":
            output.append(str(len(queue)))

        elif op == "empty":
            output.append("0" if queue else "1")

        elif op == "front":
            output.append(queue[0] if queue else "-1")

        elif op == "back":
            output.append(queue[-1] if queue else "-1")

        else:
            raise ValueError()

    return "\n".join(output)


if __name__ == "__main__":
    input_n = int(input())

    answer: str = main(input_n)
    sys.stdout.write(answer)
