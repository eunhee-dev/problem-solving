""" solve.py for 4949번. 균형잡힌 세상 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target_str: str) -> bool:
    stack = []

    for ch in target_str:
        if ch in ["(", "["]:
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif ch == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
    return not stack


def main() -> None:
    while True:
        s = sys_input()
        if s == ".":
            break

        result: bool = solve(s)
        print("yes" if result else "no")


if __name__ == "__main__":
    main()
