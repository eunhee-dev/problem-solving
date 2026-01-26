# 1431번. 시리얼 번호

## 문제
https://www.acmicpc.net/problem/1431

---

## Key Points

1. 내장함수 `sort()`의 인자 `key`에 `lambda`를 활용하여 주어진 조건을 구현하면 된다.

    - 길이: `len(x)`

    - 숫자의 합: `sum(int(x_i) for x_i in x if "0" <= x_i <= "9")`

    - 사전 순서: `x`
