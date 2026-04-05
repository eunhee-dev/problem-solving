# 0x06. 큐

## 개요

- 큐는 FIFO(First In First Out) 구조의 자료구조로, 가장 먼저 들어간 데이터가 가장 먼저 나온다.

- Python에는 STL에 queue가 없다. 보통 `collections.deque()`를 사용한다.

- deque를 queue처럼 사용할 경우에는 `deque.popleft()`와 `deque.append()`만 사용하면 된다.
    - `deque.popleft()`: front 값 제거, O(1)
    - `deque.append()`: back에 값 추가, O(1)


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 10845 | [큐](https://www.acmicpc.net/problem/10845) | [코드](./10845/) |
| 기본 문제✔ | 18258 | [큐 2](https://www.acmicpc.net/problem/18258) | [코드](./18258/) |
| 기본 문제✔ | 2164 | [카드2](https://www.acmicpc.net/problem/2164) | [코드](./2164/) |

<details>
<summary>힌트 보기</summary>

- 10845: deque 활용
- 18258: deque 활용
- 2164: deque 활용
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **list.pop(0) 금지**: `list.pop(0)`은 O(n)이므로, queue가 필요하면 반드시 `deque`를 사용한다.

- **기본 구현**: 문제 설명대로 구현하면 되는 경우가 많다. 카드2처럼 한 장 남을 때까지 반복하는 패턴.

</details>
