""" solve.py for 1431번. 시리얼 번호 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(serials: list[str]) -> list[str]:
    serials.sort(key=lambda x: (len(x), sum(int(x_i) for x_i in x if "0" <= x_i <= "9"), x))
    return serials


def main() -> None:
    n = int(sys_input())
    serials = [sys_input() for _ in range(n)]

    answer: list[str] = solve(serials)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
