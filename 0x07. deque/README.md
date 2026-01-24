# 0x07. 덱

## 개요

- 덱(Deque, Double-Ended Queue)은 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조이다.

- Python에서는 `collections.deque`를 사용한다.
    - `appendleft()`, `append()`: 양쪽 삽입 O(1)
    - `popleft()`, `pop()`: 양쪽 삭제 O(1)
    - `rotate(k)`: 회전 O(k)


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 10866 | [덱](https://www.acmicpc.net/problem/10866) | [코드](./10866번.%20덱/) |
| 기본 문제✔ | 1021 | [회전하는 큐](https://www.acmicpc.net/problem/1021) | [코드](./1021번.%20회전하는%20큐/) |
| 응용 문제✔ | 5430 | [AC](https://www.acmicpc.net/problem/5430) | [코드](./5430번.%20AC/) |
| 응용 문제 | 11003 | [최솟값 찾기](https://www.acmicpc.net/problem/11003) | [코드](./11003번.%20최솟값%20찾기/) |

<details>
<summary>힌트 보기</summary>

- 10866: 기본 구현
- 1021: rotate 활용
- 5430: reversed flag
- 11003: monotonic deque
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **Reversed Flag**: AC 문제처럼 뒤집기 연산이 많은 경우, 실제로 뒤집지 않고 flag로 방향을 관리한다.
    - flag가 True면 뒤에서 pop, False면 앞에서 popleft
    - 마지막에 출력할 때만 필요시 뒤집기

- **Monotonic Deque**: 슬라이딩 윈도우에서 최솟값/최댓값을 O(1)에 구할 때 사용한다.
    - 덱을 단조 증가/감소로 유지하면서 윈도우를 벗어난 원소는 앞에서 제거
    - 각 원소는 최대 한 번 삽입, 한 번 삭제되므로 전체 O(n)

- **빈 배열 파싱 주의**: `"".split(",")` 는 `[]`가 아닌 `[""]`이다.

</details>
