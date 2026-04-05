# 10026번. 적록색약

## 문제
https://www.acmicpc.net/problem/10026

---

## Key Points

1. 적록색약 버전과 일반 버전을 구분하여 구현한다.

2. 체크할 color를 `set()`으로 전달하여 bfs를 수행한다.

    - `is_color_blind == True` 이고 `curr_color in "RG"` 이면 `colors = {"R", "G"}`

    - 그외에는 `colors = set(curr_color)`

3. 중복과 분기가 많아져서 `bfs()` 함수를 `flood_fill()` 내부에 구현하였다.

    - `solve()` 에서는 `flood_fill()`만 호출하여 가독성을 유지
