""" solve_recursion.py for 1158번. 요세푸스 문제 """

import sys


sys.setrecursionlimit(10**4)


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_removed_recursive(n: int, k: int, curr_idx: int) -> list:
    if n == 1:
        return [0]

    next_idx = (curr_idx + k - 1) % n
    remaining_order = get_removed_recursive(n-1, k, next_idx)

    return [next_idx] + [
        idx if idx < next_idx else idx + 1
        for idx in remaining_order
    ]


def solve(n: int, k: int) -> str:
    removed = get_removed_recursive(n, k, 0)
    removed = [str(idx + 1) for idx in removed]  # 0-based to 1-based
    return "<" + ", ".join(removed) + ">"


def main() -> None:
    n, k = map(int, sys_input().split())

    answer: str = solve(n, k)
    print(answer)


if __name__ == "__main__":
    main()
