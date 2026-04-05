# 0x05. 스택

## 개요

- 스택은 LIFO(Last In First Out) 구조의 자료구조로, 가장 나중에 들어간 데이터가 가장 먼저 나온다.

- Python에서는 `list`를 스택으로 사용할 수 있다. `append()`로 push, `pop()`으로 pop.

- 스택은 괄호 매칭, 수식 계산, DFS, 백트래킹 등 다양한 문제에서 활용된다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 10828 | [스택](https://www.acmicpc.net/problem/10828) | [코드](./10828/) |
| 기본 문제✔ | 10773 | [제로](https://www.acmicpc.net/problem/10773) | [코드](./10773/) |
| 응용 문제✔ | 1874 | [스택 수열](https://www.acmicpc.net/problem/1874) | [코드](./1874/) |
| 응용 문제✔ | 2493 | [탑](https://www.acmicpc.net/problem/2493) | [코드](./2493/) |
| 응용 문제 | 6198 | [옥상 정원 꾸미기](https://www.acmicpc.net/problem/6198) | [코드](./6198/) |
| 응용 문제 | 17298 | [오큰수](https://www.acmicpc.net/problem/17298) | [코드](./17298/) |
| 응용 문제 | 3015 | [오아시스 재결합](https://www.acmicpc.net/problem/3015) | [코드](./3015/) |
| 응용 문제 | 6549 | [히스토그램에서 가장 큰 직사각형](https://www.acmicpc.net/problem/6549) | [코드](./6549/) |

<details>
<summary>힌트 보기</summary>

- 10828: 기본 구현
- 1874: monotonic stack
- 2493: 왼큰수, monotonic stack
- 6198: monotonic stack
- 17298: monotonic stack
- 3015: monotonic stack
- 6549: 오작수, monotonic stack
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **Monotonic Stack (단조 스택)**: 오큰수, 탑, 히스토그램 등의 문제에서 핵심적으로 사용된다.
    - 스택을 오름차순 또는 내림차순으로 유지하며, 조건을 만족하지 않는 원소들을 pop하면서 처리한다.
    - 각 원소가 최대 한 번 push, 한 번 pop되므로 O(n)에 처리 가능하다.

- **스택에 저장할 정보 선택**:
    - n이 작으면 `(index, value)` 튜플을 저장하는 것이 가독성이 좋다.
    - n이 크면 `index`만 저장하고 `nums[stack[-1]]`로 값에 접근하는 것이 효율적이다.

- **경계 처리**: 히스토그램 문제처럼 스택이 비었을 때의 처리, 또는 오큰수가 없는 경우의 처리에 주의한다.

- **스택 수열**: 1~n을 오름차순으로 push하면서 목표 수열을 만들 수 있는지 확인하는 문제. 불가능한 경우를 빠르게 탐지할 수 있다.

</details>
