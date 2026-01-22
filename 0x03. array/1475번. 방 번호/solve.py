""" solve.py for 1475번. 방 번호 """

import sys
import math


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n: str) -> int:
    num_list = [0] * 10

    for num in n:
        num_list[int(num)] += 1

    duplicated_cnt = (num_list[6] + num_list[9]) / 2
    num_list[6] = math.ceil(duplicated_cnt)
    num_list[9] = math.floor(duplicated_cnt)

    return max(num_list)


def main() -> None:
    n = sys_input()
    answer: int = solve(n)

    print(answer)


if __name__ == "__main__":
    main()
