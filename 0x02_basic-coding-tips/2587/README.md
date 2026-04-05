# 2587번. 대표값2

## 문제
https://www.acmicpc.net/problem/2587

---

## Key Points

1. 평균 = `sum(nums) // len(nums)` (문제에서 자연수임이 보장됨)


2. 중앙값 = 정렬 후 가운데 값. 5개이므로 `sorted(nums)[2]`.


3. `statistics` 모듈의 `mean()`, `median()`을 사용할 수도 있다.
