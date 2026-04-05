# 0x09. BFS

## 개요

- BFS(Breadth-First Search, 너비 우선 탐색)는 시작 정점에서 가까운 정점부터 순서대로 탐색하는 알고리즘이다.

- 큐를 사용하여 구현하며, 최단 거리 문제에 많이 활용된다.

- 시간복잡도: O(V + E), 공간복잡도: O(V)


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 1926 | [그림](https://www.acmicpc.net/problem/1926) | [코드](./1926/) |
| 연습 문제 | 2178 | [미로 탐색](https://www.acmicpc.net/problem/2178) | [코드](./2178/) |
| 연습 문제 | 7576 | [토마토](https://www.acmicpc.net/problem/7576) | [코드](./7576/) |
| 연습 문제 | 4179 | [불!](https://www.acmicpc.net/problem/4179) | [코드](./4179/) |
| 연습 문제 | 1697 | [숨바꼭질](https://www.acmicpc.net/problem/1697) | [코드](./1697/) |
| 기본 문제✔ | 1012 | [유기농 배추](https://www.acmicpc.net/problem/1012) | [코드](./1012/) |
| 기본 문제✔ | 10026 | [적록색약](https://www.acmicpc.net/problem/10026) | [코드](./10026/) |
| 기본 문제✔ | 7569 | [토마토](https://www.acmicpc.net/problem/7569) | [코드](./7569/) |
| 기본 문제✔ | 7562 | [나이트의 이동](https://www.acmicpc.net/problem/7562) | [코드](./7562/) |
| 기본 문제✔ | 5427 | [불](https://www.acmicpc.net/problem/5427) | [코드](./5427/) |
| 기본 문제 | 2583 | [영역 구하기](https://www.acmicpc.net/problem/2583) | [코드](./2583/) |
| 기본 문제 | 2667 | [단지번호붙이기](https://www.acmicpc.net/problem/2667) | [코드](./2667/) |
| 기본 문제 | 5014 | [스타트링크](https://www.acmicpc.net/problem/5014) | [코드](./5014/) |
| 기본 문제 | 2468 | [안전 영역](https://www.acmicpc.net/problem/2468) | [코드](./2468/) |
| 기본 문제 | 6593 | [상범 빌딩](https://www.acmicpc.net/problem/6593) | [코드](./6593/) |
| 응용 문제✔ | 2206 | [벽 부수고 이동하기](https://www.acmicpc.net/problem/2206) | [코드](./2206/) |
| 응용 문제✔ | 9466 | [텀 프로젝트](https://www.acmicpc.net/problem/9466) | [코드](./9466/) |
| 응용 문제✔ | 2573 | [빙산](https://www.acmicpc.net/problem/2573) | [코드](./2573/) |
| 응용 문제✔ | 2146 | [다리 만들기](https://www.acmicpc.net/problem/2146) | [코드](./2146/) |
| 응용 문제✔ | 13549 | [숨바꼭질 3](https://www.acmicpc.net/problem/13549) | [코드](./13549/) |
| 응용 문제✔ | 1600 | [말이 되고픈 원숭이](https://www.acmicpc.net/problem/1600) | [코드](./1600/) |
| 응용 문제 | 13913 | [숨바꼭질 4](https://www.acmicpc.net/problem/13913) | [코드](./13913/) |
| 응용 문제 | 14442 | [벽 부수고 이동하기 2](https://www.acmicpc.net/problem/14442) | [코드](./14442/) |
| 응용 문제 | 16933 | [벽 부수고 이동하기 3](https://www.acmicpc.net/problem/16933) | [코드](./16933/) |
| 응용 문제 | 16920 | [확장 게임](https://www.acmicpc.net/problem/16920) | [코드](./16920/) |
| 응용 문제 | 11967 | [불켜기](https://www.acmicpc.net/problem/11967) | [코드](./11967/) |
| 응용 문제 | 17071 | [숨바꼭질 5](https://www.acmicpc.net/problem/17071) | [코드](./17071/) |
| 응용 문제 | 9328 | [열쇠](https://www.acmicpc.net/problem/9328) | [코드](./9328/) |
| 응용 문제 | 3197 | [백조의 호수](https://www.acmicpc.net/problem/3197) | [코드](./3197/) |
| 응용 문제 | 20304 | [비밀번호 제작](https://www.acmicpc.net/problem/20304) | [코드](./20304/) |

<details>
<summary>힌트 보기</summary>

- 1926: 기본 BFS
- 2178: 최단거리
- 7576: 멀티소스 BFS
- 4179: 두 객체 동시 이동
- 1697: 1차원 BFS
- 1012: 연결 요소 개수
- 7569: 3차원 BFS
- 7562: 8방향
- 5427: 두 객체 동시 이동
- 5014: 1차원 BFS
- 6593: 3차원 BFS
- 2206: 3D BFS, 상태 확장
- 9466: 사이클 탐지
- 2146: 섬 라벨링 + BFS
- 13549: 0-1 BFS
- 1600: 3D BFS
- 13913: 경로 역추적
- 14442: 3D BFS
- 16933: 4D BFS (낮/밤)
- 16920: 멀티소스, 턴제
- 17071: 상태 압축, 홀짝
- 20304: 비트마스킹 BFS
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **기본 템플릿**: `dist` 배열로 방문 여부와 거리를 동시에 관리한다. 미방문은 -1.

- **멀티소스 BFS**: 시작점이 여러 개인 경우(토마토, 불 등), 모든 시작점을 큐에 넣고 시작한다.

- **3D BFS (상태 공간 확장)**: 벽 부수기 문제처럼 상태가 추가될 때 `dist[x][y][state]`로 차원을 확장한다.
    - 벽을 k번까지 부술 수 있으면: `dist[x][y][broken_cnt]`

- **0-1 BFS**: 가중치가 0과 1만 있을 때 다익스트라 대신 사용 (O(n)).
    - 가중치 0인 이동은 `appendleft()`, 가중치 1인 이동은 `append()`.

- **두 객체 동시 이동**: 불과 사람처럼 두 객체가 동시에 움직이는 경우, 먼저 불의 도달 시간을 계산한 `fire_map`을 만들고, 사람 BFS에서 이를 제약조건으로 사용한다.

- **경계 탈출**: 미로 탈출 문제에서 `not (0 <= nx < r and 0 <= ny < c)`가 True면 탈출 성공.

- **Python 참고**: 리스트(mutable)를 함수에 넘기면 참조가 전달되어 in-place 변경이 가능하다.

</details>
