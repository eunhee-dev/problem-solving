# 13335번. 트럭

## 문제
https://www.acmicpc.net/problem/13335

---

## Key Points

1. 다리에 트럭이 올라가는 것을 `deque()`를 통해 시뮬레이션해주면 된다.

    - 문제는 오른쪽 -> 왼쪽으로 건너지만, 나는 왼쪽 -> 오른쪽으로 구현하였다. (취향)

2. 시간을 측정할 때 다리를 기준으로해도 되고, 트럭을 기준으로 해도 된다.

    - 모든 트럭이 다리를 완전히 건널 때 까지의 시간 측정 [[풀이 - solve.py](./solve.py)]
        - 문제를 그대로 시뮬레이션 하여 더 직관적인 코드인 것 같다.
        - 실제로 구현한다면 이 방법으로 구현할 것 같다.

    - 트럭을 다 내보낼 때까지의 시간 측정 
        - 트럭을 다 내보내면 끝이 아니라, 마지막 트럭이 다리를 건너는 것 까지 고려해주어야 하는 것에 유의해야 한다.

        ```python
        def solve(w: int, l: int, trucks: deque[int]) -> int:
            total_time = 0
            bridge = deque([0] * w, maxlen=w)
            sum_bridge = 0

            while trucks:
                finished_truck = bridge.pop()
                if finished_truck:
                    sum_bridge -= finished_truck

                bridge.appendleft(0)

                if trucks[0] <= l - sum_bridge:
                    truck = trucks.popleft()
                    bridge[0] = truck
                    sum_bridge += truck
                total_time += 1

            # 마지막 트럭이 다리를 다 건너는데 걸리는 시간
            if sum_bridge != 0:
                total_time += w

            return total_time
        ```
        - 마지막 트럭이 이동하는 시뮬레이션을 스킵해서, 다리 기준보다는 약간 더 효율적인 것 같다.
  

3. `sum_bridge` 없이 매번 `sum(bridge)`를 구현해도 되지만, 덧셈이 중복되는 것이 비효율적인 것 같아 추가하였다.

    - `sum_bridge` 계산을 위해 `finished_truck`을 체크해주어야 한다.

    - `sum(bridge)`로 구현할 경우 `finished_truck`은 고려하지 않아도 된다. (O(w)가 추가되므로, w가 작을 경우 가독성 측면에서 고려해볼만 함)

    - 현재 문제에서는 w가 1000까지 될 수 있어서 `sum_bridge` 방식을 채택하였다.
