""" solve.py for 2910번. 빈도 정렬 """

import sys
from collections import Counter


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(nums: list[int]) -> list[int]:
    count = Counter(nums)
    sorted_nums = sorted(count.items(), key=lambda x: -x[1])
    return [num for num, n_cnt in sorted_nums for _ in range(n_cnt)]


def main() -> None:
    _, _ = map(int, sys_input().split())
    nums = list(map(int, sys_input().split()))

    answer: list[int] = solve(nums)
    print(*answer)


if __name__ == "__main__":
    main()
