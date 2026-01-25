""" solve_naive.py for 16235번. 나무 재테크 """

import sys
from collections import deque


DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int, a: list[list[int]], trees: list[list[int]]) -> int:
    n = len(a)
    nutrient_board = [[5] * n for _ in range(n)]
    tree_board = [[deque() for _ in range(n)] for _ in range(n)]

    trees.sort()
    for x, y, z in trees:
        tree_board[x - 1][y - 1].append(z)

    for _ in range(k):
        for x in range(n):
            for y in range(n):
                # 봄
                new_nutrient = 0
                alive_trees = deque()
                for z in tree_board[x][y]:
                    if nutrient_board[x][y] >= z:
                        nutrient_board[x][y] -= z
                        z += 1
                        alive_trees.append(z)
                    else:
                        new_nutrient += z // 2
                tree_board[x][y] = alive_trees
                # 여름
                nutrient_board[x][y] += new_nutrient

        for x in range(n):
            for y in range(n):
                # 가을
                for z in tree_board[x][y]:
                    if z % 5 == 0:
                        for dx, dy in DIRECTIONS:
                            nx, ny = x + dx, y + dy
                            if not (0 <= nx < n and 0 <= ny < n):
                                continue
                            tree_board[nx][ny].appendleft(1)
                # 겨울
                nutrient_board[x][y] += a[x][y]

    return sum(len(tree_board[x][y]) for x in range(n) for y in range(n))


def main() -> None:
    n, m, k = map(int, sys_input().split())
    a = [list(map(int, sys_input().split())) for _ in range(n)]
    trees = [list(map(int, sys_input().split())) for _ in range(m)]

    answer: int = solve(k, a, trees)
    print(answer)


if __name__ == "__main__":
    main()
