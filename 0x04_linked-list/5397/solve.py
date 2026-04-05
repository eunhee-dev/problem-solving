""" solve.py for 5397번. 키로거 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(text: str) -> str:
    left_stack = []
    right_stack = []

    for ch in text:
        if ch == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif ch == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif ch == "-":
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(ch)

    return "".join(left_stack + list(reversed(right_stack)))


def main() -> None:
    n = int(sys_input())
    for _ in range(n):
        text = sys_input()

        answer: str = solve(text)
        print(answer)


if __name__ == "__main__":
    main()
