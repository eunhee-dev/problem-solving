# 11003번. 최솟값 찾기

## 문제
https://www.acmicpc.net/problem/11003

---

## Key Points

1. 문제를 보고 바로 떠오르는 방법으로 구현하면 O(n * l)로 시간초과가 발생한다.

    ```python
    def solve(l: int, a: list) -> str:
        deq = deque([], maxlen=l)
        min_list = []

        for num in a:
            deq.append(num)
            min_list.append(str(min(deq)))

        return " ".join(min_list)
    ```

2. stack에서 썼던 monotonic stack과 같이 monotonic deque을 사용하면 O(n)에 풀이 가능하다.

3. (python에서는) 우선순위 큐(heapq, O(nlogn))으로 풀면 시간 초과가 발생한다.
