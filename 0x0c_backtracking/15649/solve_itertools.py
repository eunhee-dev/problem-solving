""" solve_itertools.py for 15649번. N과 M (1) """

import sys
from itertools import permutations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int) -> list[str]:
    perms = permutations(map(str, range(1, n+1)), m)
    return list(map(" ".join, perms))


def main() -> None:
    n, m = map(int, sys_input().split())

    answer: list[str] = solve(n, m)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
