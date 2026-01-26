""" solve.py for 11656번. 접미사 배열 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s: str) -> list[str]:
    ans = [s[i:] for i in range(len(s))]
    return sorted(ans)


def main() -> None:
    s = sys_input()

    answer: list[str] = solve(s)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
