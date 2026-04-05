# 8980번. 택배

## 문제
https://www.acmicpc.net/problem/8980

---

## Key Points

1. `tasks`를 도착지가 번호가 작은 순으로 정렬한 후, 가장 빨리 도착하는 박스를 우선으로 배송하면 된다. [[풀이 - solve.py](./solve.py)]

    - 도착지가 빠른 박스를 우선 배송하면 트럭 용량을 빨리 비워 더 많은 박스를 실을 수 있다. (그리디)

    - `used` 배열을 활용하여 출발지 ~ 도착지까지 박스의 개수를 관리할 수 있다.
        - `used[i]`: 구간 i → i+1을 지날 때 트럭에 실린 박스 수

    - $O(N \times M)$의 시간복잡도를 가진다.

2. `tasks`를 출발지 순으로 정렬한 후, max heap를 활용하여 트럭이 꽉 찼을 때 도착지가 먼 친구들을 버리는 방법도 있다. [[풀이 - solve_heapq.py](./solve_heapq.py)]

    - 발상을 전환하여 일단 박스를 실을 수 있는 만큼 싣고, 트럭이 꽉찬 경우 도착지가 가장 먼 박스 순으로 버리는 방법이 있다.

    - 결과적으로 도착지가 가까운 박스가 우선 배송되므로 풀이 1과 동일한 그리디 전략이다.

    - 도착지가 가장 먼 박스는 `max_heap`과 `dest_boxes` 리스트를 사용하면 효율적으로 관리할 수 있다.
        - `max_heap`: 현재 트럭에 실린 박스들의 도착지 관리
        - `dest_boxes[i]`: 도착지 i로 가는 박스 수

    - $O(N + M \log M)$ 의 시간복잡도를 가진다.

---

#### 풀이 2가 더 빠른 이유

풀이 1은 각 task마다 구간 전체를 순회해야 한다:
```python
for src, dest, boxes in tasks:                         # M번
    max_used = max(used[i] for i in range(src, dest))  # O(N)
    for i in range(src, dest):                         # O(N)
        used[i] += load
```

풀이 2는 마을을 한 번 순회하면서, 각 task를 heap 연산으로 처리한다:
```python
for town in range(1, n + 1):                           # N번
    while task_idx < len(tasks) and ...:               # 총 M번 (amortized)
        heapq.heappush(max_heap, -dest)                # O(log M)
```
