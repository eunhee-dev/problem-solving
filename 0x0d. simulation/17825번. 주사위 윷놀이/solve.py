""" solve.py for 17825번. 주사위 윷놀이 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(dices: list[int]) -> int:
    board = [i * 2 for i in range(21)] + [13, 16, 19, 25, 30, 35] + [22, 24] + [28, 27, 26] + [0]

    blue = [0] * 32
    blue[5], blue[10], blue[15] = 21, 27, 29

    nxt = [i + 1 for i in range(32)]
    nxt[20], nxt[26], nxt[28], nxt[31] = 32, 20, 24, 24

    max_score = 0
    pos = [0] * 4

    def backtrack(depth: int, total: int) -> None:
        nonlocal max_score
        if depth == 10:
            max_score = max(max_score, total)
            return

        for i in range(4):
            curr_pos = pos[i]

            if curr_pos == 32:
                continue

            for j in range(dices[depth]):
                if curr_pos == 32:
                    break
                if j == 0 and blue[curr_pos]:
                    curr_pos = blue[curr_pos]
                else:
                    curr_pos = nxt[curr_pos]

            if curr_pos != 32 and curr_pos in pos:
                continue

            prev_pos, pos[i] = pos[i], curr_pos
            backtrack(depth + 1, total + board[curr_pos])
            pos[i] = prev_pos

    backtrack(0, 0)
    return max_score


def main() -> None:
    dices = list(map(int, sys_input().split()))

    answer: int = solve(dices)
    print(answer)


if __name__ == "__main__":
    main()
