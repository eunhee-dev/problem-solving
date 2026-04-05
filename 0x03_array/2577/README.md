# 2577번. 숫자의 개수

## 문제
https://www.acmicpc.net/problem/2577

---

## Key Points

1. 10^9라 int 범위에 들어오지만, python은 int 범위는 신경 안써도 된다.

2. `collections`의 `Counter`를 사용하면 더 멋지게 코딩할 수 있다.

    ```python
    from collections import Counter

    def solve(a: int, b: int, c: int) -> str:
        num = str(a * b * c)
        counter = Counter(num)
        return "\n".join(str(counter.get(str(d), 0)) for d in range(10))
    ```
