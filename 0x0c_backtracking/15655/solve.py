""" solve.py for 15655번. N과 M (6) """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int, integers: list[int]) -> list[str]:
    sequences = []
    path = []
    integers.sort()

    def backtrack(start: int, depth: int) -> None:
        if depth == m:
            sequences.append(" ".join(str(integers[i]) for i in path))
            return
        for i in range(start, n):
            path.append(i)
            backtrack(i + 1, depth + 1)
            path.pop()

    backtrack(0, 0)
    return sequences


def main() -> None:
    n, m = map(int, sys_input().split())
    integers = list(map(int, sys_input().split()))

    answer: list[str] = solve(n, m, integers)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
