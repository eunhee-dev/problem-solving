# 10804번. 카드 역배치

## 문제
https://www.acmicpc.net/problem/10804

---

## Key Points

1. 초기 카드 배열은 `[1, 2, ..., 20]`이다.


2. 구간 `[a, b]`를 뒤집는 것은 파이썬 슬라이싱으로 간단히 처리: `cards[a-1:b] = cards[a-1:b][::-1]`


3. 주의: 문제의 위치는 1-indexed, 파이썬은 0-indexed이므로 `a - 1`부터 `b`까지 슬라이싱한다.
