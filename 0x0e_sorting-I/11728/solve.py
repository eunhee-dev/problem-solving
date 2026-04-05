""" solve.py for 11728번. 배열 합치기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int, a: list[int], b: list[int]) -> list[int]:
    a.sort()
    b.sort()

    c = []
    a_i, b_i = 0, 0

    while a_i < n and b_i < m:
        if a[a_i] <= b[b_i]:
            c.append(a[a_i])
            a_i += 1
        else:
            c.append(b[b_i])
            b_i += 1

    c.extend(a[a_i:])
    c.extend(b[b_i:])
    return c


def main() -> None:
    n, m = map(int, sys_input().split())
    a = list(map(int, sys_input().split()))
    b = list(map(int, sys_input().split()))

    answer: list[int] = solve(n, m, a, b)
    print(*answer)


if __name__ == "__main__":
    main()
