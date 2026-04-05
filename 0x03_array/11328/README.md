# 11328번. Strfry

## 문제
https://www.acmicpc.net/problem/11328

---

## Key Points

1. s1에서 각각의 알파벳이 몇 번 나오는지 세고, s2에서 나오는 것들을 빼준 후 모든 알파벳이 0인지 확인하면 된다.

2. 다른 개수 세는 문제들과 마찬가지로 `collections`의 `Counter`를 쓰면 더 깔끔하게 코딩 가능하다.

    ```python
    from collections import Counter

    def solve(s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)
    ```
