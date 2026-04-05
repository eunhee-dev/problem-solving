""" solve.py for 1182번. 부분수열의 합 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, s: int, integers: list[int]) -> int:
    count = 0

    def backtrack(idx: int, total: int) -> None:
        nonlocal count
        if idx == n:
            if total == s:
                count += 1
            return
        backtrack(idx + 1, total)
        backtrack(idx + 1, total + integers[idx])
        return

    backtrack(0, 0)
    return count if s != 0 else count -1


def main() -> None:
    n, s = map(int, sys_input().split())
    integers = list(map(int, sys_input().split()))

    answer: int = solve(n, s, integers)
    print(answer)


if __name__ == "__main__":
    main()
