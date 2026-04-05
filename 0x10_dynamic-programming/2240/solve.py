""" solve.py for 2240번. 자두나무 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(t: int, w: int, trees: list[int]) -> int:
    trees = [0] + trees
    dp = [[[0] * 3 for _ in range(w + 1)] for _ in range(t + 1)]
    dp[1][0][1] = 1 if trees[1] == 1 else 0
    dp[1][1][2] = 1 if trees[1] == 2 else 0

    for i in range(2, t + 1):
        for j in range(w + 1):
            plum_loc = trees[i]
            other_loc = 3 - plum_loc
            dp[i][j][other_loc] = dp[i - 1][j][other_loc]
            if j > 0:
                dp[i][j][plum_loc] = max(dp[i - 1][j][plum_loc], dp[i - 1][j - 1][other_loc]) + 1
            else:
                dp[i][j][plum_loc] = dp[i - 1][j][plum_loc] + 1

    return max(val for row in dp[t] for val in row)


def main() -> None:
    t, w = map(int, sys_input().split())
    trees = [int(sys_input()) for _ in range(t)]

    answer: int = solve(t, w, trees)
    print(answer)


if __name__ == "__main__":
    main()
