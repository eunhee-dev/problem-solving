""" Simple bfs code (with dataclass) """

from dataclasses import dataclass
from collections import deque


@dataclass
class Coord:
    x: int
    y: int


def bfs(board: list[list[int]], start: Coord = Coord(0, 0)) -> None:
    """
    Perform BFS on a 2D board starting from a given coordinate.

    Args:
        board (list): The 2D board (1: passable cells, 0: represents obstacles).
        start (Coord): Starting coordinate for BFS.
    """
    n = len(board)       # 행의 수
    m = len(board[0])    # 열의 수

    # 상, 하, 좌, 우로 이동하기 위한 방향 설정
    directions = [Coord(1, 0), Coord(0, 1), Coord(-1, 0), Coord(0, -1)]

    visited = [[False] * m for _ in range(n)]
    queue = deque([start])              # start에서 시작
    visited[start.x][start.y] = True    # start를 방문했다고 명시

    while queue:
        current = queue.popleft()
        print(f"({current.x}, {current.y}) -> ", end="")

        for direction in directions:
            nx, ny = current.x + direction.x, current.y + direction.y

            # 새로운 위치가 보드 범위를 벗어나지 않고, 이동 가능한 칸인지 확인
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append(Coord(nx, ny))

    print("")


def main() -> None:
    board = [
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    bfs(board, Coord(0, 0))


if __name__ == "__main__":
    main()
