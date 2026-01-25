""" solve_itertools.py for 1182번. 부분수열의 합 """

import sys
from itertools import combinations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, s: int, integers: list[int]) -> int:
    count = 0

    for k in range(1, n+1):
        for comb in combinations(integers, k):
            if sum(comb) == s:
                count += 1

    return count


def main() -> None:
    n, s = map(int, sys_input().split())
    integers = list(map(int, sys_input().split()))

    answer: int = solve(n, s, integers)
    print(answer)


if __name__ == "__main__":
    main()
