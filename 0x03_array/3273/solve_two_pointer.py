""" solve_two_pointer.py for 3273번. 두 수의 합 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: list[int], x: int) -> int:
    a.sort()

    left = 0
    right = len(a) - 1
    cnt = 0

    while left < right:
        candidate = a[left] + a[right]
        if candidate == x:
            cnt += 1
            left += 1
            right -= 1
        elif candidate > x:
            right -= 1
        else:
            left += 1

    return cnt


def main() -> None:
    _ = int(sys_input())
    a = list(map(int, sys_input().split()))
    x = int(sys_input())

    answer: int = solve(a, x)
    print(answer)


if __name__ == "__main__":
    main()
