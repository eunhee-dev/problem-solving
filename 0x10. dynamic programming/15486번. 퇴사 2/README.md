# 15486번. 퇴사 2

## 문제
https://www.acmicpc.net/problem/15486

---

## Key Points

1. [14501번. 퇴사](../14501번.%20퇴사/) 문제의 풀이에서 `max(dp[:i])`를 기록해두면 O(n)에 풀이 가능하다.

    - i가 1부터 순차적으로 증가하기 때문에, `max(dp[:i])`를 매번 구하지 말고, `max_profit` 변수에 기록해두면 된다.

    - `max_profit = max(max_profit, dp[i])`
