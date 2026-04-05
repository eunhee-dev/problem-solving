""" solve.py for 9466번. 텀 프로젝트 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(choice: list[int], visited: list[bool], start: int) -> int:
    queue = deque([start])
    visited[start] = True
    visit_path = [start]

    while queue:
        x = queue.popleft()
        nx = choice[x]
        if visited[nx]:  # 방문할 노드가 이미 방문한 노드이면, 싸이클 확인 후 탐색 종료
            if nx in visit_path:  # 싸이클 확인
                cycle_start = visit_path.index(nx)
                visit_path = visit_path[:cycle_start]  # 싸이클은 팀을 이루기 때문에 no_team 에서 제외
            break
        visited[nx] = True
        queue.append(nx)
        visit_path.append(nx)
    return len(visit_path)


def solve(n: int, choice: list[int]) -> int:
    visited = [False] * n
    no_team_cnt = 0
    for student in range(n):
        if not visited[student]:
            no_team_cnt += bfs(choice, visited, student)
    return no_team_cnt


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        n = int(sys_input())
        choice = [int(x) -1 for x in sys_input().split()]

        answer: int = solve(n, choice)
        print(answer)


if __name__ == "__main__":
    main()
