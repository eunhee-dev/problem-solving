# 13913번. 숨바꼭질 4

## 문제
https://www.acmicpc.net/problem/13913

---

## Key Points

1. [1697번. 숨바꼭질](../1697번.%20숨바꼭질/) 문제에서 경로 추적만 더 하면 되는 문제

2. `prev_history`라는 배열을 두어 bfs를 돌릴 때 `prev_history[nx] = x` 를 저장해두고, 나중에 k 부터 n이 될 때까지 역으로 꺼내면 경로 복원 가능
