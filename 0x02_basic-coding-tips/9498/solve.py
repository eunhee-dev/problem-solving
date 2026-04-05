""" solve.py for 9498번. 시험 성적 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(score: int) -> str:
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


def main() -> None:
    score = int(sys_input())

    answer: str = solve(score)
    print(answer)


if __name__ == "__main__":
    main()
