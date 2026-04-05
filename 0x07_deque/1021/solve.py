""" solve.py for 1021번. 회전하는 큐 """

from collections import deque


def solve(n: int, nums: list[int]) -> int:
    deq = deque(range(1, n + 1))
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


def main() -> None:
    n, _ = map(int, input().split())
    nums = list(map(int, input().split()))

    answer: int = solve(n, nums)
    print(answer)


if __name__ == "__main__":
    main()
