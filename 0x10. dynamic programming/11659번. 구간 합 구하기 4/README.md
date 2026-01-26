# 11659번. 구간 합 구하기 4

## 문제
https://www.acmicpc.net/problem/11659

---

## Key Points

1. dp를 사용해서 구간 합을 구할 수 있다.

    - dp[i]: i번째 까지 수열의 합

    - `dp[i] = dp[i - 1] + seq[i]`

2. 미리 구해둔 구간 합을 이용하여 start ~ end 까지의 구간합을 쉽게 구할 수 있다.

    - start ~ end 까지의 합: `dp[end] - dp[start - 1]`
