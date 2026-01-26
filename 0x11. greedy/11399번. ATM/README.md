# 11399번. ATM

## 문제
https://www.acmicpc.net/problem/11399

---

## Key Points

1. 시간이 누적되기 때문에, 오름차순으로 p를 정렬하는 것이 최솟값이다.

    - 누적 합은 `itertools.accumulate()`를 활용하여 간결하게 구할 수 있다.
