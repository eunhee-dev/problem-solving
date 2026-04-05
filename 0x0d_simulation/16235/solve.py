""" solve.py for 16235번. 나무 재테크 """

import sys
from collections import defaultdict


DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int, a: list[list[int]], trees: list[list[int]]) -> int:
    n = len(a)
    nutrient_board = [[5] * n for _ in range(n)]
    tree_board = [[defaultdict(int) for _ in range(n)] for _ in range(n)]

    for x, y, z in trees:
        tree_board[x - 1][y - 1][z] += 1

    for _ in range(k):
        for x in range(n):
            for y in range(n):
                if not tree_board[x][y]:
                    continue
                # 봄
                survive_trees = defaultdict(int)
                new_nutrient = 0
                no_nutrient = False
                for z, tree_count in sorted(tree_board[x][y].items()):
                    if tree_count == 0:
                        continue

                    if no_nutrient:
                        new_nutrient += (z // 2) * tree_count
                        continue

                    survive_tree_count = nutrient_board[x][y] // z
                    if tree_count <= survive_tree_count:
                        nutrient_board[x][y] -= z * tree_count
                        survive_trees[z + 1] = tree_count
                    else:
                        no_nutrient = True
                        nutrient_board[x][y] -= z * survive_tree_count
                        survive_trees[z + 1] += survive_tree_count
                        new_nutrient += (z // 2) * (tree_count - survive_tree_count)
                tree_board[x][y] = survive_trees

                #여름
                nutrient_board[x][y] += new_nutrient

        for x in range(n):
            for y in range(n):
                # 가을
                if tree_board[x][y]:
                    new_tree_count = 0
                    for z, tree_count in tree_board[x][y].items():
                        if z % 5 == 0:
                            new_tree_count += tree_count

                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue
                        tree_board[nx][ny][1] += new_tree_count

                # 겨울
                nutrient_board[x][y] += a[x][y]

    return sum(sum(tree_board[x][y].values()) for x in range(n) for y in range(n))


def main() -> None:
    n, m, k = map(int, sys_input().split())
    a = [list(map(int, sys_input().split())) for _ in range(n)]
    trees = [list(map(int, sys_input().split())) for _ in range(m)]

    answer: int = solve(k, a, trees)
    print(answer)


if __name__ == "__main__":
    main()
