""" solve.py for 10807번. 개수 세기 """

import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(s: list[str], v: str) -> bool:
    return s.count(v)


def main() -> None:
    _ = sys_input()
    s = sys_input().split()
    v = sys_input()

    answer: int = solve(s, v)
    print(answer)


if __name__ == "__main__":
    main()
