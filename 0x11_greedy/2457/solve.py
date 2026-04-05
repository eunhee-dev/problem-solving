""" solve.py for 2457번. 공주님의 정원 """

import sys
from itertools import accumulate


MONTH_TO_DAYS = list(accumulate([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def date_to_days(m: int, d: int) -> int:
    return MONTH_TO_DAYS[m - 1] + d


def solve(n: int, flowers: list[tuple[int, int]]) -> int:
    flowers.sort()

    start_date = date_to_days(3, 1)
    end_date = date_to_days(11, 30)

    curr_end = start_date
    count = 0
    idx = 0

    while curr_end <= end_date:
        max_curr_end = curr_end

        while idx < n and flowers[idx][0] <= curr_end:
            if flowers[idx][1] > max_curr_end:
                max_curr_end = flowers[idx][1]
            idx += 1

        # (기간에 공백이 생기지 않게 하는) 꽃을 찾지 못한 경우
        if max_curr_end == curr_end:
            return 0

        count += 1
        curr_end = max_curr_end

    return count


def main() -> None:
    n = int(sys_input())
    flowers = [(date_to_days(x[0], x[1]), date_to_days(x[2], x[3]))
               for x in (list(map(int, sys_input().split())) for _ in range(n))]

    answer: int = solve(n, flowers)
    print(answer)


if __name__ == "__main__":
    main()
