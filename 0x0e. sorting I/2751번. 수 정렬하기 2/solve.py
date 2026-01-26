""" solve.py for 2751번. 수 정렬하기 2 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def merge(a: list[int], b: list[int]) -> list[int]:
    c = []
    a_i, b_i = 0, 0

    while a_i < len(a) and b_i < len(b):
        if a[a_i] <= b[b_i]:
            c.append(a[a_i])
            a_i += 1
        else:
            c.append(b[b_i])
            b_i += 1

    c.extend(a[a_i:])
    c.extend(b[b_i:])
    return c


def solve(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    merged_arr = []

    mid = len(arr) // 2
    left_half = solve(arr[:mid])
    right_half = solve(arr[mid:])

    merged_arr.extend(merge(left_half, right_half))
    return merged_arr


def main() -> None:
    n = int(sys_input())
    arr = list(int(sys_input()) for _ in range(n))

    answer: list[int] = solve(arr)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
