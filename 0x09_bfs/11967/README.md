# 11967번. 불켜기

## 문제
https://www.acmicpc.net/problem/11967

---

## Key Points

1. 현재 좌표에서 킬 수 있는 방을 다 켜고, 불을 켠 방 상하좌우로 이전에 방문한 적이 있으면 그 좌표를 바로 큐에 넣어줌
    - 이렇게 해야 불을 켠 방에 바로 이동할 수 있음

2. 현재 좌표에서 상하좌우로 불 켜진 방 중에 방문 안 한 곳이 있는지 체크
    - 불을 켰을 때는 못갔던 방을 방문할 수 있음

3. 구현 팁

    - switch를 (x, y) 튜플을 키로 하는 딕셔너리로 만들면 참조가 쉬움 (`switch = {(x, y): (a, b)}`)

    - `defaultdict`를 사용하면 key가 없는 경우에도 지정한 type으로 초기화 시켜줘 코드가 간결해짐
        ```python
        # defaultdict 사용
        switch = defaultdict(list)
        for _ in range(m):
            x, y, a, b = map(int, sys_input().split())
            switch[(x-1, y-1)].append((a-1, b-1))

        # dict 사용
        switch = {}
        for _ in range(m):
            x, y, a, b = map(int, sys_input().split())
            if (x-1, y-1) not in switch:
                switch[(x-1, y-1)] = [(a-1, b-1)]
            else:
                switch[(x-1, y-1)].append((a-1, b-1))
        ```
