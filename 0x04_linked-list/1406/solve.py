""" solve.py for 1406번. 에디터 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(text: str, m: int) -> str:
    left_stack = list(text)
    right_stack = []

    for _ in range(m):
        cmd = sys_input().split()
        op = cmd[0]

        if op == "L":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif op == "D":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif op == "B":
            if left_stack:
                left_stack.pop()
        elif op == "P":
            left_stack.append(cmd[1])

    return "".join(left_stack + list(reversed(right_stack)))


def main() -> None:
    text = sys_input()
    m = int(sys_input())

    answer: str = solve(text, m)
    print(answer)


if __name__ == "__main__":
    main()
