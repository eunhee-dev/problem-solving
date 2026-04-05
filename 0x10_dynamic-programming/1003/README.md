# 1003번. 피보나치 함수

## 문제
https://www.acmicpc.net/problem/1003

---

## Key Points

1. 2차원 DP를 사용하여, 0과 1의 출력 개수를 기록하면 되는 문제이다.

    - dp[0][i]: `fibonacci(i)`가 0을 출력하는 개수

    - dp[1][i]: `fibonacci(i)`가 1을 출력하는 개수

    - 피보나치 함수이므로, dp 배열 둘 다 피보나치 점화식을 따름
