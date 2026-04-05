# 0x10. 다이나믹 프로그래밍

## 개요

- 다이나믹 프로그래밍(DP)은 큰 문제를 작은 부분 문제로 나누어 해결하고, 결과를 저장(메모이제이션)하여 중복 계산을 피하는 기법이다.

- 점화식을 세우는 것이 핵심이며, Bottom-up(반복문)과 Top-down(재귀+메모이제이션) 두 가지 방식이 있다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 1463 | [1로 만들기](https://www.acmicpc.net/problem/1463) | [코드](./1463/) |
| 연습 문제 | 9095 | [1, 2, 3 더하기](https://www.acmicpc.net/problem/9095) | [코드](./9095/) |
| 연습 문제 | 2579 | [계단 오르기](https://www.acmicpc.net/problem/2579) | [코드](./2579/) |
| 연습 문제 | 1149 | [RGB거리](https://www.acmicpc.net/problem/1149) | [코드](./1149/) |
| 연습 문제 | 11726 | [2×n 타일링](https://www.acmicpc.net/problem/11726) | [코드](./11726/) |
| 연습 문제 | 11659 | [구간 합 구하기 4](https://www.acmicpc.net/problem/11659) | [코드](./11659/) |
| 연습 문제 | 12852 | [1로 만들기 2](https://www.acmicpc.net/problem/12852) | [코드](./12852/) |
| 기본 문제✔ | 1003 | [피보나치 함수](https://www.acmicpc.net/problem/1003) | [코드](./1003/) |
| 기본 문제✔ | 1932 | [정수 삼각형](https://www.acmicpc.net/problem/1932) | [코드](./1932/) |
| 기본 문제✔ | 11727 | [2×n 타일링 2](https://www.acmicpc.net/problem/11727) | [코드](./11727/) |
| 기본 문제✔ | 2193 | [이친수](https://www.acmicpc.net/problem/2193) | [코드](./2193/) |
| 기본 문제✔ | 1912 | [연속합](https://www.acmicpc.net/problem/1912) | [코드](./1912/) |
| 기본 문제✔ | 11055 | [가장 큰 증가하는 부분 수열](https://www.acmicpc.net/problem/11055) | [코드](./11055/) |
| 기본 문제✔ | 11053 | [가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053) | [코드](./11053/) |
| 기본 문제✔ | 9461 | [파도반 수열](https://www.acmicpc.net/problem/9461) | [코드](./9461/) |
| 기본 문제✔ | 14501 | [퇴사](https://www.acmicpc.net/problem/14501) | [코드](./14501/) |
| 기본 문제✔ | 15486 | [퇴사 2](https://www.acmicpc.net/problem/15486) | [코드](./15486/) |
| 기본 문제✔ | 10844 | [쉬운 계단 수](https://www.acmicpc.net/problem/10844) | [코드](./10844/) |
| 기본 문제 | 2748 | [피보나치 수 2](https://www.acmicpc.net/problem/2748) | [코드](./2748/) |
| 기본 문제 | 2240 | [자두나무](https://www.acmicpc.net/problem/2240) | [코드](./2240/) |
| 기본 문제 | 14002 | [가장 긴 증가하는 부분 수열 4](https://www.acmicpc.net/problem/14002) | [코드](./14002/) |
| 기본 문제 | 2156 | [포도주 시식](https://www.acmicpc.net/problem/2156) | [코드](./2156/) |
| 기본 문제 | 15988 | [1, 2, 3 더하기 3](https://www.acmicpc.net/problem/15988) | [코드](./15988/) |
| 기본 문제 | 2302 | [극장 좌석](https://www.acmicpc.net/problem/2302) | [코드](./2302/) |
| 기본 문제 | 11052 | [카드 구매하기](https://www.acmicpc.net/problem/11052) | [코드](./11052/) |
| 기본 문제 | 9465 | [스티커](https://www.acmicpc.net/problem/9465) | [코드](./9465/) |
| 기본 문제 | 11057 | [오르막 수](https://www.acmicpc.net/problem/11057) | [코드](./11057/) |
| 기본 문제 | 2293 | [동전 1](https://www.acmicpc.net/problem/2293) | [코드](./2293/) |
| 기본 문제 | 1904 | [01타일](https://www.acmicpc.net/problem/1904) | [코드](./1904/) |
| 기본 문제 | 1788 | [피보나치 수의 확장](https://www.acmicpc.net/problem/1788) | [코드](./1788/) |
| 기본 문제 | 4883 | [삼각 그래프](https://www.acmicpc.net/problem/4883) | [코드](./4883/) |

<details>
<summary>힌트 보기</summary>

- 1463: 기본 DP
- 9095: 기본 DP
- 2579: 2D DP 또는 1D DP
- 1149: 2D DP
- 11726: 피보나치 변형
- 11659: 누적 합
- 12852: 경로 역추적
- 1003: 메모이제이션
- 1932: 2D DP
- 1912: 카데인 알고리즘
- 11055: LIS 변형
- 11053: LIS
- 10844: 2D DP
- 2156: 계단 오르기 변형
- 2293: 배낭 문제 변형
- 14002: LIS + 경로 역추적
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **점화식 설계**: `dp[i]`가 무엇을 의미하는지 명확히 정의하는 것이 가장 중요하다.

- **상태 확장 (2차원 DP)**: 추가 조건이 있으면 `dp[i][j]`처럼 차원을 확장한다.
    - 계단 오르기: `dp[i][j]` = i번째 계단을 j번 연속 밟아서 올라왔을 때 최대 점수

- **LIS (가장 긴 증가하는 부분 수열)**:
    - O(n²): `dp[i]` = i번째로 끝나는 LIS 길이
    - O(n log n): 이분 탐색 활용

- **발상의 전환**: 밟지 않을 계단의 최소값을 구하는 등 문제를 반대로 생각하면 풀리는 경우도 있다.

</details>
