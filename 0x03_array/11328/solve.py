""" solve.py for 11328번. Strfry """

import sys
import string


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s1: str, s2: str) -> bool:
    s = {ch: 0 for ch in string.ascii_lowercase}
    for ch in s1:
        s[ch] += 1
    for ch in s2:
        s[ch] -= 1
    return not any(s.values())


def main() -> None:
    n = int(sys_input())
    for _ in range(n):
        s1, s2 = sys_input().split()
        answer: bool = solve(s1, s2)

        if answer:
            print("Possible")
        else:
            print("Impossible")


if __name__ == "__main__":
    main()
