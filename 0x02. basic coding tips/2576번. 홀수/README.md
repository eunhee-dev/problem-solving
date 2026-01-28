# 2576번. 홀수

## 문제
https://www.acmicpc.net/problem/2576

---

## Key Points

1. `% 2 == 1` 또는 `& 1`로 홀수 판별이 가능하다.


2. 홀수 리스트를 먼저 필터링한 후, `sum()`과 `min()`으로 처리한다.


3. 홀수가 없는 경우(`if not odds`)를 먼저 처리해야 한다.
