# 1149번. RGB거리

## 문제
https://www.acmicpc.net/problem/1149

---

## Key Points

1. 색깔이 3가지 있으므로, 2차원 dp를 사용하면 쉽게 해결 가능하다.

    - dp[i][color]: i번째 집을 color로 칠할 때 총 비용의 최소 값

    - i-1번째 집을 color가 아닌 색으로 칠했을 때 총 비용의 최소값 + i번째 집을 color로 칠하는 비용을 하면 됨

    - `dp[i][color] = min(dp[i-1][j] for j in range(3) if j != color) + cost[i][color]`
