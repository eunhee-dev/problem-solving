# 1932번. 정수 삼각형

## 문제
https://www.acmicpc.net/problem/1932

---

## Key Points

1. DP를 이용하여, 현재 꼭지점을 선택했을 때 얻을 수 있는 최대값을 계산해나가면 되는 문제이다.

    - dp[x][y]: x행 y열 꼭지점을 골랐을 때 얻을 수 있는 최대값

    - `dp[x][y] = max(dp[x + 1][y], dp[x + 1][y + 1]) + triangle[x][y]`

2. `dp` 배열을 따로 만들지 않고, `triangle`에 in-place로 바로 반영하면 더 간단하게 구현 가능하다. (현재 문제와 같이 `triangle`의 원본이 필요 없을 경우)
