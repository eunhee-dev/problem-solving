# 11057번. 오르막 수

## 문제
https://www.acmicpc.net/problem/11057

---

## Key Points

1. 끝자리를 기록해두는 2차원 dp 배열을 사용하면 된다.

    - dp[i][j]: j로 끝나는 길이 i의 오르막 수의 개수

    - dp[i][j]는 dp[i - 1][0] ~ dp[i - 1][j]의 합이다. (0 ~ j로 끝나는 길이 i-1의 오르막 수에 j를 붙이면 되기 때문에)

    - `dp[i][j] = sum(dp[i - 1][k])` (0 <= k <= j)

