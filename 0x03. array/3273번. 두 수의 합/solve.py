""" solve.py for 3273번. 두 수의 합 """

import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(a: list[int], x: int) -> int:
    candidate = set()
    count = 0

    for a_i in a:
        if a_i in candidate:
            count += 1
            candidate.remove(a_i)
        else:
            candidate.add(x - a_i)
    return count


def main() -> None:
    _ = sys_input()
    a = list(map(int, sys_input().split()))
    x = int(sys_input())

    answer: int = solve(a, x)
    print(answer)


if __name__ == "__main__":
    main()
