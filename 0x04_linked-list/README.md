# 0x04. 연결 리스트

## 개요

- Python에는 STL에 linked list가 없다.

- 따라서, linked list 문제를 풀 때는 직접 구현해야 하는데 이는 상당히 번거로운 과정이다.

- 또한 linked list를 Python level에서 구현하게 되면, C로 구현되어 있는 STL 자료구조(e.g. deque)를 쓰는 것보다 오히려 비효율적일 수 있다.

- 따라서 최대한 linked list 없이 풀 수 있는 방법을 찾아보는 것이 좋다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 1406 | [에디터](https://www.acmicpc.net/problem/1406) | [코드](./1406/) |
| 기본 문제✔ | 5397 | [키로거](https://www.acmicpc.net/problem/5397) | [코드](./5397/) |
| 기본 문제✔ | 1158 | [요세푸스 문제](https://www.acmicpc.net/problem/1158) | [코드](./1158/) |

<details>
<summary>힌트 보기</summary>

- 1406: double stack
- 5397: double stack
- 1158: deque.rotate()
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **Double Stack**: 에디터/키로거처럼 커서가 한 칸씩만 이동하는 문제는 두 개의 스택을 활용하면 효율적으로 풀 수 있다.
    - 커서 왼쪽 문자들을 담는 스택, 오른쪽 문자들을 담는 스택

- **Deque 활용**: 요세푸스 문제처럼 원형 구조에서 회전이 필요한 경우 `deque.rotate()`를 활용한다.
    - 이론적 시간복잡도가 같아도, C로 구현된 deque가 Python level linked list보다 훨씬 빠르다.

- **입출력 최적화**: 입력이 많은 문제(n, m이 10만 이상)에서는 `sys.stdin.readline()`을 사용해야 시간 초과를 피할 수 있다.

- **재귀 제한**: 백준에서는 `sys.getrecursionlimit()`이 1000으로 설정되어 있으므로, 재귀 깊이가 깊어질 수 있는 문제는 `sys.setrecursionlimit()`으로 조정해야 한다.

</details>
