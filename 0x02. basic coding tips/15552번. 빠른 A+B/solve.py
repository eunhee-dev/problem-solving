""" solve.py for 15552번. 빠른 A+B """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(pairs: list[tuple[int, int]]) -> list[int]:
    return [a + b for a, b in pairs]


def main() -> None:
    t = int(sys_input())
    pairs = [(a, b) for a, b in (map(int, sys_input().split()) for _ in range(t))]

    result: list[int] = solve(pairs)
    sys.stdout.write("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
