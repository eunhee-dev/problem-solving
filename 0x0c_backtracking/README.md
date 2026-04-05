# 0x0c. 백트래킹

## 개요

- 백트래킹은 모든 경우의 수를 탐색하되, 가망이 없는 경로는 조기에 포기(pruning)하는 기법이다.

- 재귀를 사용하여 상태를 변경하고, 되돌아올 때 상태를 복원하는 것이 핵심이다.

- 순열, 조합, 부분집합 등의 완전탐색 문제에 많이 활용된다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 15649 | [N과 M (1)](https://www.acmicpc.net/problem/15649) | [코드](./15649/) |
| 연습 문제 | 9663 | [N-Queen](https://www.acmicpc.net/problem/9663) | [코드](./9663/) |
| 연습 문제 | 1182 | [부분수열의 합](https://www.acmicpc.net/problem/1182) | [코드](./1182/) |
| 기본 문제✔ | 15650 | [N과 M (2)](https://www.acmicpc.net/problem/15650) | [코드](./15650/) |
| 기본 문제✔ | 15651 | [N과 M (3)](https://www.acmicpc.net/problem/15651) | [코드](./15651/) |
| 기본 문제✔ | 15652 | [N과 M (4)](https://www.acmicpc.net/problem/15652) | [코드](./15652/) |
| 기본 문제✔ | 15654 | [N과 M (5)](https://www.acmicpc.net/problem/15654) | [코드](./15654/) |
| 기본 문제✔ | 15655 | [N과 M (6)](https://www.acmicpc.net/problem/15655) | [코드](./15655/) |
| 기본 문제✔ | 15656 | [N과 M (7)](https://www.acmicpc.net/problem/15656) | [코드](./15656/) |
| 기본 문제✔ | 15657 | [N과 M (8)](https://www.acmicpc.net/problem/15657) | [코드](./15657/) |
| 기본 문제✔ | 15663 | [N과 M (9)](https://www.acmicpc.net/problem/15663) | [코드](./15663/) |
| 기본 문제✔ | 15664 | [N과 M (10)](https://www.acmicpc.net/problem/15664) | [코드](./15664/) |
| 기본 문제✔ | 15665 | [N과 M (11)](https://www.acmicpc.net/problem/15665) | [코드](./15665/) |
| 기본 문제✔ | 15666 | [N과 M (12)](https://www.acmicpc.net/problem/15666) | [코드](./15666/) |
| 기본 문제✔ | 6603 | [로또](https://www.acmicpc.net/problem/6603) | [코드](./6603/) |
| 기본 문제 | 1759 | [암호 만들기](https://www.acmicpc.net/problem/1759) | [코드](./1759/) |
| 응용 문제✔ | 1941 | [소문난 칠공주](https://www.acmicpc.net/problem/1941) | [코드](./1941/) |
| 응용 문제✔ | 16987 | [계란으로 계란치기](https://www.acmicpc.net/problem/16987) | [코드](./16987/) |
| 응용 문제 | 18809 | [Gaaaaaaaaaarden](https://www.acmicpc.net/problem/18809) | - |
| 응용 문제 | 1799 | [비숍](https://www.acmicpc.net/problem/1799) | - |

<details>
<summary>힌트 보기</summary>

- 15649: 순열
- 9663: 대각선 체크
- 1182: 부분집합
- 15650: 조합
- 15651: 중복순열
- 15652: 중복조합
- 15663: 중복 제거
- 15664: 중복 제거
- 15665: 중복 제거
- 15666: 중복 제거
- 6603: 조합
- 1759: 조합 + 조건
- 1941: 조합 + BFS
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **상태 복원**: 재귀에서 돌아올 때 `pop()` + `is_used[i] = False`로 상태를 원래대로 복원해야 모든 경우를 탐색할 수 있다.

- **is_used 배열**: N과 M 시리즈에서는 숫자 중복 사용을 방지하기 위해 `is_used` 배열을 사용한다.

- **N-Queen 체크 배열**: 퀸 문제에서는 행, 열, 대각선 각각에 대해 체크 배열이 필요하다.
    - 열: `is_used_col[col]`
    - ↙ 대각선: `is_used_diag1[row + col]`
    - ↘ 대각선: `is_used_diag2[row - col + (n - 1)]`

- **nonlocal 활용**: `solve()` 내부에서 `backtrack()` 함수를 정의하고, `nonlocal count`로 외부 함수의 변수를 갱신할 수 있다.

- **itertools 활용**: 연습 목적이 아니라면 `permutations`, `combinations`를 사용하면 간단히 구현 가능.

</details>
