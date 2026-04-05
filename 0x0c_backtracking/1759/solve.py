""" solve.py for 1759번. 암호 만들기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(l: int, c: int, chars: list[str]) -> list[str]:
    sequences = []
    path = []
    vowels = {"a", "e", "i", "o", "u"}
    chars.sort()

    def backtrack(start: int, depth: int) -> None:
        if depth == l:
            v_cnt = sum(1 for ch in path if ch in vowels)
            cons_cnt = l - v_cnt
            if v_cnt >= 1 and cons_cnt >= 2:
                sequences.append("".join(path))
            return
        for i in range(start, c):
            path.append(chars[i])
            backtrack(i + 1, depth + 1)
            path.pop()

    backtrack(0, 0)
    return sequences


def main() -> None:
    l, c = map(int, sys_input().split())
    chars = sys_input().split()

    answer: list[str] = solve(l, c, chars)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
