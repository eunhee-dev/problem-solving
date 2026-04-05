# 9095번. 1, 2, 3 더하기

## 문제
https://www.acmicpc.net/problem/9095

---

## Key Points

1. dp[i]: i를 1, 2, 3의 합으로 나타내는 방법의 가지수

    - `dp[i - 1]`에서 1을 더하거나, `dp[i - 2]`에서 2를 더하거나, `dp[i - 3]`에서 3을 더하면 되기 때문에, `dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]`
