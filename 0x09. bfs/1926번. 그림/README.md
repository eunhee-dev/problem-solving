# 1926번. 그림

## 문제
https://www.acmicpc.net/problem/1926

---

## Key Points

1. 방문하지 않은 지점을 시작점으로 하여 bfs를 수행하고 방문한 노드 수(size)를 리턴한다.

2. paints_size 배열을 만들어 bfs의 return 값을 저장하고, len()과 max()로 답을 구한다.

    - max() 사용 시 paints_size가 빈 배열일 수 있음을 고려한 예외처리 필요

3. bfs() 함수에 visited 배열을 인자로 넘기면, bfs()에서 visited를 in-place 변경한다.

    - 리스트 같은 mutable object는 함수에 인자로 넘기면 "참조"가 전달됨

    - 따라서 따로 visited를 반환하지 않아도 됨

    - docstring에 이러한 내용을 남겨두면 협업 (또는 나중에 내가 봤을 때) 혼란을 줄일 수 있다.
