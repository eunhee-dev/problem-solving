""" solve.py for 1021번. 회전하는 큐 """ 

from collections import deque


def solve(n: int, _: int, nums:list) -> int:
    deq  = deque(range(1, n + 1))
    min_count = 0

    for num in nums:
        idx = deq.index(num)

        if idx < n - idx:
            for _ in range(idx):
                deq.append(deq.popleft())
            min_count += idx
        else:
            for _ in range(n - idx):
                deq.appendleft(deq.pop())
            min_count += n - idx

        deq.popleft()
        n -= 1

    return min_count


if __name__ == "__main__":
    input_n, input_m = map(int, input().split())
    input_nums = list(map(int, input().split()))

    answer: int = solve(input_n, input_m, input_nums)
    print(answer)
