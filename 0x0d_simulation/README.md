# 0x0d. 시뮬레이션

## 개요

- 시뮬레이션은 문제에서 주어진 상황을 그대로 구현하는 문제 유형이다.

- 삼성 SW 역량테스트에서 자주 출제되며, 구현력을 테스트한다.

- 복잡한 조건과 예외 처리를 정확히 구현하는 것이 핵심이다.


## 문제 풀이 현황

> 삼성 SW 역량테스트 기출 문제가 대부분으로, 총 60개의 문제가 포함되어 있습니다.

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 15683 | [감시](https://www.acmicpc.net/problem/15683) | [코드](./15683/) |
| 연습 문제 | 18808 | [스티커 붙이기](https://www.acmicpc.net/problem/18808) | [코드](./18808/) |
| 연습 문제 | 12100 | [2048 (Easy)](https://www.acmicpc.net/problem/12100) | [코드](./12100/) |
| 연습 문제 | 15686 | [치킨 배달](https://www.acmicpc.net/problem/15686) | [코드](./15686/) |
| 기본 문제✔ | 11559 | [Puyo Puyo](https://www.acmicpc.net/problem/11559) | [코드](./11559/) |
| 기본 문제✔ | 14891 | [톱니바퀴](https://www.acmicpc.net/problem/14891) | [코드](./14891/) |
| 기본 문제✔ | 14499 | [주사위 굴리기](https://www.acmicpc.net/problem/14499) | [코드](./14499/) |
| 기본 문제✔ | 13335 | [트럭](https://www.acmicpc.net/problem/13335) | [코드](./13335/) |
| 기본 문제✔ | 16985 | [Maaaaaaaaaze](https://www.acmicpc.net/problem/16985) | [코드](./16985/) |
| 기본 문제✔ | 14503 | [로봇 청소기](https://www.acmicpc.net/problem/14503) | [코드](./14503/) |
| 기본 문제✔ | 3190 | [뱀](https://www.acmicpc.net/problem/3190) | [코드](./3190/) |
| 기본 문제✔ | 14500 | [테트로미노](https://www.acmicpc.net/problem/14500) | [코드](./14500/) |
| 기본 문제✔ | 13460 | [구슬 탈출 2](https://www.acmicpc.net/problem/13460) | [코드](./13460/) |
| 기본 문제✔ | 14502 | [연구소](https://www.acmicpc.net/problem/14502) | [코드](./14502/) |
| 기본 문제✔ | 14888 | [연산자 끼워넣기](https://www.acmicpc.net/problem/14888) | [코드](./14888/) |
| 기본 문제✔ | 14889 | [스타트와 링크](https://www.acmicpc.net/problem/14889) | [코드](./14889/) |
| 기본 문제✔ | 14890 | [경사로](https://www.acmicpc.net/problem/14890) | [코드](./14890/) |
| 기본 문제✔ | 15684 | [사다리 조작](https://www.acmicpc.net/problem/15684) | [코드](./15684/) |
| 기본 문제✔ | 15685 | [드래곤 커브](https://www.acmicpc.net/problem/15685) | [코드](./15685/) |
| 기본 문제 | 17281 | [⚾](https://www.acmicpc.net/problem/17281) | [코드](./17281/) |
| 기본 문제 | 5373 | [큐빙](https://www.acmicpc.net/problem/5373) | [코드](./5373/) |
| 기본 문제 | 16234 | [인구 이동](https://www.acmicpc.net/problem/16234) | [코드](./16234/) |
| 기본 문제 | 16235 | [나무 재테크](https://www.acmicpc.net/problem/16235) | [코드](./16235/) |
| 기본 문제 | 16236 | [아기 상어](https://www.acmicpc.net/problem/16236) | [코드](./16236/) |
| 기본 문제 | 17140 | [이차원 배열과 연산](https://www.acmicpc.net/problem/17140) | [코드](./17140/) |
| 기본 문제 | 17141 | [연구소 2](https://www.acmicpc.net/problem/17141) | [코드](./17141/) |
| 기본 문제 | 17142 | [연구소 3](https://www.acmicpc.net/problem/17142) | [코드](./17142/) |
| 기본 문제 | 17143 | [낚시왕](https://www.acmicpc.net/problem/17143) | [코드](./17143/) |
| 기본 문제 | 17144 | [미세먼지 안녕!](https://www.acmicpc.net/problem/17144) | [코드](./17144/) |
| 기본 문제 | 4991 | [로봇 청소기](https://www.acmicpc.net/problem/4991) | [코드](./4991/) |
| 기본 문제 | 16986 | [인싸들의 가위바위보](https://www.acmicpc.net/problem/16986) | [코드](./16986/) |
| 기본 문제 | 17779 | [게리맨더링 2](https://www.acmicpc.net/problem/17779) | [코드](./17779/) |
| 기본 문제 | 17837 | [새로운 게임 2](https://www.acmicpc.net/problem/17837) | [코드](./17837/) |
| 기본 문제 | 17822 | [원판 돌리기](https://www.acmicpc.net/problem/17822) | [코드](./17822/) |
| 기본 문제 | 17825 | [주사위 윷놀이](https://www.acmicpc.net/problem/17825) | [코드](./17825/) |
| 기본 문제 | 19235 | [모노미노도미노](https://www.acmicpc.net/problem/19235) | [코드](./19235/) |
| 기본 문제 | 20061 | [모노미노도미노 2](https://www.acmicpc.net/problem/20061) | [코드](./20061/) |
| 기본 문제 | 19236 | [청소년 상어](https://www.acmicpc.net/problem/19236) | [코드](./19236/) |
| 기본 문제 | 19237 | [어른 상어](https://www.acmicpc.net/problem/19237) | [코드](./19237/) |
| 기본 문제 | 19238 | [스타트 택시](https://www.acmicpc.net/problem/19238) | [코드](./19238/) |
| 기본 문제 | 20055 | [컨베이어 벨트 위의 로봇](https://www.acmicpc.net/problem/20055) | [코드](./20055/) |
| 기본 문제 | 20056 | [마법사 상어와 파이어볼](https://www.acmicpc.net/problem/20056) | [코드](./20056/) |
| 기본 문제 | 20057 | [마법사 상어와 토네이도](https://www.acmicpc.net/problem/20057) | [코드](./20057/) |
| 기본 문제 | 20058 | [마법사 상어와 파이어스톰](https://www.acmicpc.net/problem/20058) | [코드](./20058/) |
| 기본 문제 | 16637 | [괄호 추가하기](https://www.acmicpc.net/problem/16637) | [코드](./16637/) |
| 기본 문제 | 17070 | [파이프 옮기기 1](https://www.acmicpc.net/problem/17070) | [코드](./17070/) |
| 기본 문제 | 17135 | [캐슬 디펜스](https://www.acmicpc.net/problem/17135) | [코드](./17135/) |
| 기본 문제 | 17136 | [색종이 붙이기](https://www.acmicpc.net/problem/17136) | [코드](./17136/) |
| 기본 문제 | 17406 | [배열 돌리기 4](https://www.acmicpc.net/problem/17406) | [코드](./17406/) |
| 기본 문제 | 17471 | [게리맨더링](https://www.acmicpc.net/problem/17471) | [코드](./17471/) |
| 기본 문제 | 17472 | [다리 만들기 2](https://www.acmicpc.net/problem/17472) | [코드](./17472/) |
| 기본 문제 | 15898 | [피아의 아틀리에 ~신비한 대회의 연금술사~](https://www.acmicpc.net/problem/15898) | [코드](./15898/) |
| 기본 문제 | 21608 | [상어 초등학교](https://www.acmicpc.net/problem/21608) | [코드](./21608/) |
| 기본 문제 | 21609 | [상어 중학교](https://www.acmicpc.net/problem/21609) | [코드](./21609/) |
| 기본 문제 | 21610 | [마법사 상어와 비바라기](https://www.acmicpc.net/problem/21610) | [코드](./21610/) |
| 기본 문제 | 21611 | [마법사 상어와 블리자드](https://www.acmicpc.net/problem/21611) | [코드](./21611/) |
| 기본 문제 | 23288 | [주사위 굴리기 2](https://www.acmicpc.net/problem/23288) | [코드](./23288/) |
| 기본 문제 | 23289 | [온풍기 안녕!](https://www.acmicpc.net/problem/23289) | [코드](./23289/) |
| 기본 문제 | 23290 | [마법사 상어와 복제](https://www.acmicpc.net/problem/23290) | [코드](./23290/) |
| 기본 문제 | 23291 | [어항 정리](https://www.acmicpc.net/problem/23291) | [코드](./23291/) |
| 기본 문제 | 2478 | [자물쇠](https://www.acmicpc.net/problem/2478) | [코드](./2478/) |


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **문제 분해**: 복잡한 문제는 여러 단계로 나누어 생각한다.
    - 연구소: 빈 칸 조합 → 벽 세우기 → 바이러스 전파 → 안전영역 계산
    - 뱀: 이동 → 종료 조건 체크 → 사과 처리 → 방향 회전

- **보드 복사 vs Undo**: 시뮬레이션마다 보드를 새로 만들거나, 변경 후 원복(undo)하는 방식을 선택한다.
    - 보드가 작으면 복사가 더 간단하고 빠를 수 있다.

- **방향 회전**: `DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]`처럼 정의하고, 인덱스 ±1로 회전 처리.

- **deque로 상태 관리**: 뱀처럼 머리/꼬리가 있는 객체는 deque로 관리하면 편하다.

- **itertools 활용**: 조합, 순열이 필요한 경우 `combinations`, `permutations` 활용.

</details>
