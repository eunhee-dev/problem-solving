# 0x0f. 정렬 II

## 개요

- 정렬 I에서 배운 기본 정렬을 응용하여 더 복잡한 조건의 정렬 문제를 해결한다.

- 다중 조건 정렬, 커스텀 비교 함수, 정렬 후 이분 탐색 활용 등을 다룬다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 1431 | [시리얼 번호](https://www.acmicpc.net/problem/1431) | [코드](./1431/) |
| 연습 문제 | 11652 | [카드](https://www.acmicpc.net/problem/11652) | [코드](./11652/) |
| 기본 문제✔ | 5648 | [역원소 정렬](https://www.acmicpc.net/problem/5648) | [코드](./5648/) |
| 기본 문제✔ | 1181 | [단어 정렬](https://www.acmicpc.net/problem/1181) | - |
| 기본 문제✔ | 2910 | [빈도 정렬](https://www.acmicpc.net/problem/2910) | [코드](./2910/) |
| 기본 문제 | 10814 | [나이순 정렬](https://www.acmicpc.net/problem/10814) | - |
| 기본 문제 | 11656 | [접미사 배열](https://www.acmicpc.net/problem/11656) | [코드](./11656/) |
| 기본 문제 | 10825 | [국영수](https://www.acmicpc.net/problem/10825) | [코드](./10825/) |
| 응용 문제✔ | 7795 | [먹을 것인가 먹힐 것인가](https://www.acmicpc.net/problem/7795) | [코드](./7795/) |

<details>
<summary>힌트 보기</summary>

- 1431: 다중 조건
- 11652: Counter
- 2910: Counter + 정렬
- 11656: 문자열 정렬
- 10825: 다중 조건
- 7795: 정렬 + 이분탐색
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **다중 조건 정렬**: `key=lambda x: (조건1, 조건2, ...)` 형태로 우선순위를 정의한다.

- **커스텀 정렬**: 특수한 비교 기준이 필요하면 `functools.cmp_to_key` 사용.

- **빈도 정렬**: `Counter`로 빈도를 세고, 빈도 기준으로 정렬.

- **정렬 + 이분탐색**: 정렬 후 `bisect`로 O(log n) 탐색 가능.

</details>
