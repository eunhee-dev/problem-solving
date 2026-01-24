# 2468번. 안전 영역

## 문제
https://www.acmicpc.net/problem/2468

---

## Key Points

1. 기본 bfs 문제가 `board[x][y] == 1`일 때 방문할 수 있다면, 해당 문제는 `board[x][y] > rain` 일 때 방문할 수 있다.

2. rain의 범위는 `range(0, max_height)`이며, 각 rain에 대해 bfs를 수행하여 max 값을 찾는다.

    - 비가 안 내릴 수도 있다... 따라서 0부터 시작한다...

    - `max_count = 1`로 시작하면 `range(1, max_height)`도 무방하다.
        - 0일 때 bfs 탐색을 안하니 약간의 최적화도 챙길 수 있다.
