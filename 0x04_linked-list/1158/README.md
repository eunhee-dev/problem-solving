# 1158번. 요세푸스 문제

## 문제
https://www.acmicpc.net/problem/1158

---

## Key Points

1. 직접 linked list를 구현해도 O(n * k)에 풀이 가능하지만 (탐색: O(K), n번 반복: O(n * k)), `deque.rotate()`을 사용하는 것 또한 O(n * k)에 가능하다.

2. linked list vs. deque

    - python으로 linked list를 구현하면 python level에서 실행

    - 반면 deque는 C로 구현되어 있는 메소드 실행

    - 따라서 이론적으로 시간복잡도가 같아도, 구현 레벨에서의 차이 때문에 deque를 사용하는 것이 더욱 효율적임

3. 재귀로 푸는 방법을 생각해 볼 수 있지만, deque을 사용하는 것에 비해 재귀 함수를 호출하는 것 자체가 overhead가 상당하다. (마찬가지로 python level)
    
    - 풀이 설명
        - 현재 배열에서 제거할 인덱스 `next_idx` 계산
        - `next_idx`에서 시작해 남은 배열에 대해 재귀함수 호출
        - 반환된 리스트에서 인덱스를 보정하여 최종 제거 순서를 생성 (`next_idx`보다 크거나 같으면 1을 더함)

    - 백준에서는 `sys.getrecursionlimit()` 값이 1000으로 설정되어 있음, n이 5000 이하이므로 10**4 정도 세팅해주어야 함
