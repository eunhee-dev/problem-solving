""" solve.py for 15663번. N과 M (9) """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int, integers: list[int]) -> list[str]:
    sequences = []
    path = []
    is_used = [False] * n
    integers.sort()

    def backtrack(depth: int) -> None:
        if depth == m:
            sequences.append(" ".join(str(integers[i]) for i in path))
            return

        prev = 0
        for i in range(n):
            if not is_used[i]:
                curr = integers[i]
                if prev == curr:
                    continue

                is_used[i] = True
                path.append(i)
                prev = curr

                backtrack(depth + 1)

                path.pop()
                is_used[i] = False

    backtrack(0)
    return sequences


def main() -> None:
    n, m = map(int, sys_input().split())
    integers = list(map(int, sys_input().split()))

    answer: list[str] = solve(n, m, integers)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
