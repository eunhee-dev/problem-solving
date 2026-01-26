""" solve.py for 1744번. 수 묶기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(sequence: list[int]) -> int:
    total = 0
    sequence.sort()

    pos_seq = []
    neg_seq = []

    for num in sequence:
        if num <= 0:
            neg_seq.append(num)
        elif num == 1:
            total += 1
        else:
            pos_seq.append(num)

    pos_seq.reverse()

    for i in range(0, len(pos_seq), 2):
        if i + 1 < len(pos_seq):
            total += pos_seq[i] * pos_seq[i + 1]
        else:
            total += pos_seq[i]

    for i in range(0, len(neg_seq), 2):
        if i + 1 < len(neg_seq):
            total += neg_seq[i] * neg_seq[i + 1]
        else:
            total += neg_seq[i]

    return total


def main() -> None:
    n = int(sys_input())
    sequence = [int(sys_input()) for _ in range(n)]

    answer: int = solve(sequence)
    print(answer)


if __name__ == "__main__":
    main()
