""" solve.py for 9012번. 괄호 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(paren_str: str) -> bool:
    if len(paren_str) % 2:
        return False

    paren_cnt = 0

    for ch in paren_str:
        if ch == "(":
            paren_cnt += 1
        elif ch == ")":
            paren_cnt -= 1

        if paren_cnt < 0:
            return False

    return paren_cnt == 0


def main() -> None:
    n = int(sys_input())

    for _ in range(n):
        paren_str = sys_input()

        result: bool = solve(paren_str)
        print("YES" if result else "NO")


if __name__ == "__main__":
    main()
