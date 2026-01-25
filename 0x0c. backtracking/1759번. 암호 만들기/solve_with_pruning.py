""" solve_with_pruning.py for 1759번. 암호 만들기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(l: int, c: int, chars: list[str]) -> list[str]:
    sequences = []
    path = []
    vowels = {"a", "e", "i", "o", "u"}
    chars.sort()

    def backtrack(start: int, depth: int, v_cnt: int, cons_cnt: int) -> None:
        if c - start < l - depth:
            return
        if cons_cnt + (l - depth) < 2:
            return

        if depth == l:
            if v_cnt >= 1 and cons_cnt >= 2:
                sequences.append("".join(path))
            return
        for i in range(start, c):
            ch = chars[i]
            path.append(ch)
            if ch in vowels:
                backtrack(i + 1, depth + 1, v_cnt + 1, cons_cnt)
            else:
                backtrack(i + 1, depth + 1, v_cnt, cons_cnt + 1)
            path.pop()

    backtrack(0, 0, 0, 0)
    return sequences


def main() -> None:
    l, c = map(int, sys_input().split())
    chars = sys_input().split()

    answer: list[str] = solve(l, c, chars)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
