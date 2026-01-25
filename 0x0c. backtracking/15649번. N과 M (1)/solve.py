""" solve.py for 15649번. N과 M (1) """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int) -> list[str]:
    sequences = []
    path = []
    is_used = [False] * (n + 1)

    def backtrack(depth: int) -> None:
        if depth == m:
            sequences.append(" ".join(map(str, path)))
            return
        for i in range(1, n+1):
            if not is_used[i]:
                is_used[i] = True
                path.append(i)
                backtrack(depth + 1)
                path.pop()
                is_used[i] = False

    backtrack(0)
    return sequences


def main() -> None:
    n, m = map(int, sys_input().split())

    answer: list[str] = solve(n, m)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
