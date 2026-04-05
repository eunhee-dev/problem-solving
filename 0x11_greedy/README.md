# 0x11. 그리디

## 개요

- 그리디 알고리즘은 매 순간 최적이라고 생각되는 선택을 하여 최종 해답에 도달하는 기법이다.

- 항상 최적해를 보장하지는 않으므로, 그리디로 풀 수 있는지 증명이 필요하다.

- 정렬 후 그리디하게 선택하는 패턴이 많다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 11047 | [동전 0](https://www.acmicpc.net/problem/11047) | [코드](./11047/) |
| 연습 문제 | 1931 | [회의실 배정](https://www.acmicpc.net/problem/1931) | [코드](./1931/) |
| 연습 문제 | 2217 | [로프](https://www.acmicpc.net/problem/2217) | [코드](./2217/) |
| 연습 문제 | 1026 | [보물](https://www.acmicpc.net/problem/1026) | [코드](./1026/) |
| 기본 문제✔ | 11399 | [ATM](https://www.acmicpc.net/problem/11399) | [코드](./11399/) |
| 기본 문제✔ | 2457 | [공주님의 정원](https://www.acmicpc.net/problem/2457) | [코드](./2457/) |
| 기본 문제✔ | 1541 | [잃어버린 괄호](https://www.acmicpc.net/problem/1541) | [코드](./1541/) |
| 기본 문제✔ | 11501 | [주식](https://www.acmicpc.net/problem/11501) | [코드](./11501/) |
| 기본 문제✔ | 1744 | [수 묶기](https://www.acmicpc.net/problem/1744) | [코드](./1744/) |
| 기본 문제 | 2847 | [게임을 만든 동준이](https://www.acmicpc.net/problem/2847) | [코드](./2847/) |
| 기본 문제 | 1439 | [뒤집기](https://www.acmicpc.net/problem/1439) | [코드](./1439/) |
| 기본 문제 | 11000 | [강의실 배정](https://www.acmicpc.net/problem/11000) | [코드](./11000/) |
| 기본 문제 | 15903 | [카드 합체 놀이](https://www.acmicpc.net/problem/15903) | [코드](./15903/) |
| 응용 문제✔ | 2170 | [선 긋기](https://www.acmicpc.net/problem/2170) | [코드](./2170/) |
| 응용 문제✔ | 1700 | [멀티탭 스케줄링](https://www.acmicpc.net/problem/1700) | [코드](./1700/) |
| 응용 문제 | 8980 | [택배](https://www.acmicpc.net/problem/8980) | [코드](./8980/) |
| 응용 문제 | 7570 | [줄 세우기](https://www.acmicpc.net/problem/7570) | [코드](./7570/) |

<details>
<summary>힌트 보기</summary>

- 11047: 기본 그리디
- 1931: 끝나는 시간 정렬
- 11399: 오름차순 정렬
- 1541: 문자열 파싱
- 2217: 내림차순 정렬
- 1744: 양수/음수 분리
- 11501: 뒤에서부터
- 11000: 힙 활용
- 1700: 최적 페이지 교체
- 2170: 구간 병합
- 15903: 힙 활용
- 7570: LIS 변형
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **회의실 배정**: 끝나는 시간이 가장 빠른 순으로 정렬 후 그리디하게 선택.
    - `(끝나는 시간, 시작 시간)` 순으로 정렬하면 시작=끝 케이스도 처리됨.

- **최적 페이지 교체 (멀티탭 스케줄링)**: 앞으로 가장 늦게 사용될 것을 교체.

- **그리디 vs DP**: 그리디처럼 보이지만 DP로 풀어야 하는 문제들이 있으니 주의.

</details>


## 그리디 같아 보이는 문제

### [12865번. 평범한 배낭](https://www.acmicpc.net/problem/12865)

- 무게 대비 가치가 높은 물건을 우선으로 그리디하게 고르면 될 것 같지만, 배낭의 무게에 한계가 있어 반례가 존재한다.
    - items = [(6, 7), (5, 4), (5, 5)], k = 10 이면 그리디 풀이는 7, 실제 정답은 9이다.

- DP를 활용하여 풀이한다. ([0-1 knapsack 문제](https://namu.wiki/w/배낭%20문제))
    - 상세 풀이
        <details>
        <summary> 점화식 </summary>

        - `dp[i][w]`: 처음 i개의 물건으로 무게 w만큼 담을 때의 최대 가치
        - `dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_w] + item_v)`
        </details>

        <details>
        <summary> 코드 </summary>

        ```python
        import sys


        def sys_input() -> str:
            return sys.stdin.readline().rstrip()


        def solve(n: int, k: int, items: list[tuple[int, int]]) -> int:
            items = [(0, 0)] + items

            dp = [[0] * (k + 1) for _ in range(n + 1)]

            for i in range(1, n + 1):
                for w in range(1, k + 1):
                    item_w, item_v = items[i]
                    if item_w <= w:
                        dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_w] + item_v)
                    else:
                        dp[i][w] = dp[i - 1][w]

            return dp[n][k]


        def main() -> None:
            n, k = map(int, sys_input().split())
            items = [(x[0], x[1]) for x in (list(map(int, sys_input().split())) for _ in range(n))]

            answer: int = solve(n, k, items)
            print(answer)


        if __name__ == "__main__":
            main()

        ```
        </details>


### [1477번. 휴게소 세우기](https://www.acmicpc.net/problem/1477)

- 언뜻보면 단순한 그리디 문제로, 가장 긴 구간의 가운데에 휴게소를 세우면 될 것 같아 보이지만 아래와 같은 반례가 존재한다.

    - 단순한 그리디: 각각의 휴게소를 세울 때, 가장 긴 구간의 가운데에 휴게소를 세운다.

    - n=0, m=2, l=100 일 때 단순한 그리디로 풀면 50 -> 25 위치 순서로 휴게소를 세워 최대 구간이 50이 되지만, 실제 최적해는 [33, 66] 위치에 휴게소를 세워 34

    - 단순한 그리디는 현재 가장 긴 구간만 보고 무작정 가운데에 세우지만, 이 문제의 경우 여러 구간에 휴게소를 어떻게 분배할지가 중요함

- 이 문제의 경우 parametric search를 활용하여 풀 수 있다. (아직 배우지 않음)

    - parametric search
        <details>
        <summary> 설명 </summary>

        - 최적화 문제를 결정 문제(decision problem)으로 변환하여 해결하는 알고리즘

        - 핵심 아이디어
            1. 결정 문제로 전환: "최적값을 구하라" -> "값 X로 가능한가?"
            2. 이분 탐색 적용: 가능/불가능의 경계를 이분 탐색으로 찾음
            3. 단조성(Monotonicity): 어떤 값 X가 가능하면, 그보다 큰(or 작은) 값도 가능해야 함

        </details>
        <br>

    - 상세 풀이
        <details>
        <summary> 핵심 풀이 </summary>

        - 결정 문제: 구간 길이가 `d`이고, 최대 `x` 이하로 만들고 싶을 때 필요한 휴게소의 개수는?
            - `(d - 1) // x`: 길이 d인 구간을 `x` 이하로 만들기 위해 필요한 휴게소 수
            - 모든 구간의 합이 m 이하면 → `x`로 가능
            - `sum((d - 1) // x for d in dist) <= m`
            - 위 조건을 만족하는 최소 `x`를 이분 탐색으로 찾음

        - 전체 시간복잡도: O($NlogL$)

        </details>

        <details>
        <summary>코드</summary>

        ```python
        """solve_parametric_search.py for 1477번. 휴게소 세우기"""

        import sys


        def sys_input() -> str:
            return sys.stdin.readline().rstrip()


        def solve(n: int, m: int, l: int, service_areas: list[int]) -> int:
            service_areas.sort()
            service_areas = [0] + service_areas + [l]
            dist = [service_areas[i + 1] - service_areas[i] for i in range(n + 1)]

            lo = 1
            hi = max(dist)
            while lo < hi:
                mid = (lo + hi) // 2
                if sum((d - 1) // mid for d in dist) <= m:
                    hi = mid
                else:
                    lo = mid + 1

            return lo


        def main() -> None:
            n, m, l = map(int, sys_input().split())
            service_areas = list(map(int, sys_input().split()))

            answer: int = solve(n, m, l, service_areas)
            print(answer)


        if __name__ == "__main__":
            main()

        ```
        </details>

- 그럼에도 불구하고, 이 문제의 경우 그리디하게 풀이가 가능하다.

    - 그리디 풀이
        <details>
        <summary> 핵심 풀이 </summary>
        
        - 아이디어: 매번 "현재 최대 구간"을 선택하고, 그 구간을 균등 분할했을 때의 최대 길이로 갱신

        - 그리디 가능한 이유: 최종 답 = 모든 구간 중 최댓값이므로, 가장 긴 구간을 줄이지 않으면 그게 병목이 됨. 즉, 구간을 균등하게 나눌수록 최대 길이가 작아진다.
            - 모든 구간 중 최대 값을 균등하게 분배한다.
            - `new_dist = math.ceil(dist[i] / (count[i] + 1))`
                - `dist[i]`: i번 구간의 최초 길이
                - `count[i]`: i번 구간에 설치할 휴게소 개수
            - 예. n=0, m=2, l=100 일 때, 0번 구간에 휴게소 2개를 균등하게 설치하면 부분 구간의 최대 길이는 `math.ceil(100 / 3)` => 34 이다.

        - 우선순위 큐를 활용하여 가장 긴 구간을 O($logN$)에 선택할 수 있다.

        - 전체 시간복잡도: O($mlogN$)

        - 문제 조건에서 M이 클 수록 Parametric Search 풀이가 유리하고, N이나 L이 클 수록 그리디 풀이가 유리하다. (현재 문제 조건에서는 비슷함)

        </details>

        <details>
        <summary> 코드 </summary>

        ```python
        """solve_greedy.py for 1477번. 휴게소 세우기"""

        import sys
        import heapq
        import math


        def sys_input() -> str:
            return sys.stdin.readline().rstrip()


        def solve(n: int, m: int, l: int, service_areas: list[int]) -> int:
            service_areas.sort()
            service_areas = [0] + service_areas + [l]
            dist = [service_areas[i + 1] - service_areas[i] for i in range(n + 1)]

            count = [0] * (n + 1)
            heap = [(-d, i) for i, d in enumerate(dist)]
            heapq.heapify(heap)

            for _ in range(m):
                _, i = heapq.heappop(heap)
                count[i] += 1
                new_dist = math.ceil(dist[i] / (count[i] + 1))
                heapq.heappush(heap, (-new_dist, i))

            return -heap[0][0]


        def main() -> None:
            n, m, l = map(int, sys_input().split())
            service_areas = list(map(int, sys_input().split()))

            answer: int = solve(n, m, l, service_areas)
            print(answer)


        if __name__ == "__main__":
            main()

        ```

        </details>
