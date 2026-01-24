# 9466번. 텀 프로젝트

## 문제
https://www.acmicpc.net/problem/9466

---

## Key Points

1. dfs가 좀 더 어울리는 문제이지만, bfs 스타일(?)로 풀이하였음 (방향이 하나라 결국 비슷함)

2. 방문하지 않은 노드에 대해 bfs 수행하여 team을 못이루는 학생의 수를 구함

    - bfs: 방문할 노드가 이미 방문한 노드이면, 싸이클이 있는지 확인
        - 싸이클이 있으면: 방문 경로 중 싸이클 시작 지점을 찾아 그 전까지의 길이 return
        - 싸이클이 없으면: 방문 경로 길이 return

3. 원래는 코드를 아래와 같이 짰었는데, 시간 초과 발생

    ``` python
    # time exceeded code snippet

    def bfs():
        # ...
        while queue:
            x = queue.popleft()
            nx = choice[x]
            if nx in visit_path:  # 매 반복마다 검사 수행 (비효율적)
                cycle_start = visit_path.index(nx)
                return len(visit_path[:cycle_start])
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
                visit_path.append(nx)
        return len(visit_path)
    ```

    - 풀이 코드와 로직상으로 크게 다른 점이 없어 보이나, 매 반복마다 `if nx in path`를 수행하여 O(n**2)의 시간복잡도 발생

    - 풀이 코드의 경우, `if visited[nx]` 인 경우에만 `if nx in path`를 수행하기 때문에 더 효율적임

    - `if x in list` 와 같은 비싼 연산을 추가로 사용할 때는 효율성을 더 고려해야 함
