# 11652번. 카드

## 문제
https://www.acmicpc.net/problem/11652

---

## Key Points

1. 카드를 정렬하고, 숫자를 세어 가장 높은 빈도로 등장하는 카드를 출력하면 된다.

2. `sort()` 와 `collections.Counter`를 사용하여 해결할 수 있다.

    - 풀이에서는 딕셔너리의 value를 기준으로 최대 값을 구하기 위해  Counter의 메소드인 `most_common()`을 사용했지만, `max()`의 `key`를 사용해도 된다. (`max(count, key=count.get)`)

    - 정렬이 되어있기 때문에, 빈도가 같으면 제일 작은 값을 return 한다.

3. python은 int가 사실상 무한이기 때문에, integer overflow를 고려하지 않아도 된다.
