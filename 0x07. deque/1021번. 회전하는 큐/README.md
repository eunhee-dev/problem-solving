# 1021번. 회전하는 큐

## 문제
https://www.acmicpc.net/problem/1021

---

## Key Points

1. 이 문제의 경우 n이 50 이하로 매우 작아서, deque보다 list를 쓰는게 아주 미세하게 빠를 수도 있다.

    - n이 너무 작아 `deque.popleft()` python 레벨 메소드 호출 비용 > `list.pop(0)` C 레벨 함수 (`memmove`) 단순 호출

    - list는 연속배열, deque는 linked list라서 `list.index()` < `deque.index()`

    - 이러한 차이들로 n이 매우 작을때 list의 효율성이 약간 역전되는 현상 발생

2. 그러나 n이 커지면 당연히도 deque가 훨씬 유리하니 맨 앞/뒤 삽입/삭제는 deque를 사용하자.
