""" solve.py for 6603번. 로또 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int, s: list[str]) -> list[str]:
    sequences = []
    path = []

    def backtrack(depth: int) -> None:
        if depth == 6:
            sequences.append(" ".join(s[i] for i in path))
            return
        for i in range(k):
            if path and path[-1] >= i:
                continue
            path.append(i)
            backtrack(depth + 1)
            path.pop()

    backtrack(0)
    return sequences


def main() -> None:
    while True:
        test_case = sys_input().split()
        if test_case[0] == "0":
            break
        k = int(test_case[0])
        s = test_case[1:]
        answer: list[str] = solve(k, s)
        print(*answer, sep="\n")
        print()


if __name__ == "__main__":
    main()
