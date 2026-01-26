# 11726번. 2×n 타일링

## 문제
https://www.acmicpc.net/problem/11726

---

## Key Points

1. 2xi 사각형을 채우는 방법은 i-1까지 채운 사각형에 2x1을 붙이거나, i-2까지 채운 사각형에 1x2를 2개 붙이는 방법이 있다.

    - `dp[i] = dp[i - 1] + dp[i - 2]`

    - 피보나치와 동일한 점화식

2. python은 integer overflow가 없어 10007를 마지막에 나눠줘도 되지만, 성능을 위해서라도 10007로 미리 나눠놓는게 좋다.
