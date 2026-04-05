""" solve.py for 15650번. N과 M (2) """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int) -> list[str]:
    sequences = []
    path = []

    def backtrack(start: int, depth: int) -> None:
        if depth == m:
            sequences.append(" ".join(map(str, path)))
            return
        for i in range(start, n+1):
            path.append(i)
            backtrack(i + 1, depth + 1)
            path.pop()

    backtrack(1, 0)
    return sequences


def main() -> None:
    n, m = map(int, sys_input().split())

    answer: list[str] = solve(n, m)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
