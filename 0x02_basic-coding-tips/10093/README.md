# 10093번. 숫자

## 문제
https://www.acmicpc.net/problem/10093

---

## Key Points

1. A와 B의 대소관계가 정해지지 않았으므로 `min()`/`max()` 처리가 필요하다.


2. "사이"는 양 끝을 제외하므로 `range(min+1, max)`로 구한다.


3. 개수는 `max - min - 1`로 계산할 수 있다.
