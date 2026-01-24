""" Simple bfs code (with tuple) """

from collections import deque


def bfs(board: list[list[int]], start: tuple[int, int]) -> None:
    """
    Perform BFS on a 2D board starting from a given coordinate.

    Args:
        board (list): The 2D board (1: passable cells, 0: represents obstacles).
        start (tuple): Starting coordinate for BFS.
    """
    n = len(board)       # 행의 수
    m = len(board[0])    # 열의 수

    # 상, 하, 좌, 우로 이동하기 위한 방향 설정
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    start_x, start_y = start

    visited = [[False] * m for _ in range(n)]
    queue = deque([(start_x, start_y)])  # start에서 시작
    visited[start_x][start_y] = True     # start를 방문했다고 명시

    while queue:
        x, y = queue.popleft()
        print(f"({x}, {y}) -> ", end="")

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 새로운 위치가 보드 범위를 벗어나지 않고, 이동 가능한 칸인지 확인
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

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
    bfs(board, (0, 0))


if __name__ == "__main__":
    main()
