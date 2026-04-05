# 4179번. 불!

## 문제
https://www.acmicpc.net/problem/4179

---

## Key Points

1. 불에 대한 bfs를 먼저 돌려 `fire_map`을 확보하고, `fire_map`을 제약조건으로 지훈이에 대해 bfs를 돌려 탈출할 수 있는지 확인힌다.

    - `fire_map`: 불이 붙은 시간을 표시한 지도

    - `nt`: 지훈이가 해당 칸에 도달하는 최소 시간 (`dist[x][y] + 1`)

    - 지훈이의 bfs에서는 다음 차례에 방문할 `fire_map[nx][ny]`이 `nt` 보다 작은지 추가로 확인

2. 문제에 불이 여러 군데 붙어서 시작하는지, 불이 아예 안 붙어 있을지에 대해 명시해주지 않아 전부 고려해줘야 한다.

    - 불이 여러군데 붙어서 시작하는 경우 처리: 멀티소스 bfs (큐에 다 넣고 시작하기, [7576번. 토마토](../7576/))

    - 불이 아예 안 붙어 있을 경우 처리: `fire_map[nx][ny] != -1`을 먼저 체크
        - 안해주면, `fire_map[nx][ny] <= nt`가 무조건 True가 됨

3. 지훈이 bfs를 다 돌리고, 양 끝 row와 column에 `-1`이 아닌 제일 작은 수를 찾는 방법이 먼저 떠오를 수 있다. (모두 `-1`이면 IMPOSSIBLE)

    - 하지만, bfs 조건 중에 `if not (0 <= nx < r and 0 <= ny < c)`가 이미 끝점에 도달했음을 의미함

    - 이 경우 바로 `nt`를 return 해주면 끝까지 돌지 않아도 됨

4. bfs 코드가 겹쳐, bfs를 하나로 통합하는 방법도 고려해보았다.

    - 더 복잡해지는 것 같아, 지금 단계에서는 분리하는 것이 더 좋을 것 같음

    ```python
    def bfs(r: int, c: int, maze: list[str], starts: list[tuple[int, int]],
            fire_map: list[list[int]] | None = None) -> list[list[int]] | int | None:
        dist = [[-1] * c for _ in range(r)]
        queue = deque(starts)
        for start_x, start_y in starts:
            dist[start_x][start_y] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                nt = dist[x][y] + 1
                if not (0 <= nx < r and 0 <= ny < c):
                    if fire_map:
                        return nt
                    continue
                if maze[nx][ny] == "#":
                    continue
                if dist[nx][ny] != -1:
                    continue
                if fire_map and fire_map[nx][ny] != -1 and fire_map[nx][ny] <= dist[x][y] + 1:
                    continue

                dist[nx][ny] = nt
                queue.append((nx, ny))

        return dist if not fire_map else None
    ```
