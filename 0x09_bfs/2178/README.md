# 2178번. 미로 탐색

## 문제
https://www.acmicpc.net/problem/2178

---

## Key Points

1. visited 대신 dist를 사용하여 거리를 표시하면 된다.
    - `bool` (True/False) 대신 `int` (dist[x][y] + 1)

2. dist를 -1로 초기화 하면 `방문 여부`와 `거리` 구분이 더 명확해진다.
