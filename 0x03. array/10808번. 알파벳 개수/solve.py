""" solve.py for 110808번. 알파벳 개수 """

import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(s: str) -> list[int]:
    alphabet_lower = [0] * (ord("z") - ord("a") + 1)  # 26
    for ch in s:
        alphabet_lower[ord(ch) - ord("a")] += 1
    return alphabet_lower


def main() -> None:
    s = sys_input()

    answer: list[int] = solve(s)
    print(*answer)


if __name__ == "__main__":
    main()
