""" solve_itertools.py for 1759번. 암호 만들기 """

import sys
from itertools import combinations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(l: int, chars: list[str]) -> list[str]:
    sequences = []
    chars.sort()
    vowels = {"a", "e", "i", "o", "u"}
    for comb in combinations(chars, l):
        v_cnt = sum(1 for ch in comb if ch in vowels)
        cons_cnt = l - v_cnt
        if v_cnt >= 1 and cons_cnt >= 2:
            sequences.append("".join(comb))
    return sequences


def main() -> None:
    l, _ = map(int, sys_input().split())
    chars = sys_input().split()

    answer: list[str] = solve(l, chars)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
