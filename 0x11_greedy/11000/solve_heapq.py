import sys
import heapq


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(time_table: list[list[int]]) -> int:
    time_table.sort(key=lambda x: x[0])

    rooms = []
    heapq.heappush(rooms, time_table[0][1])

    for s, t in time_table[1:]:
        if rooms[0] <= s:
            heapq.heappop(rooms)
        heapq.heappush(rooms, t)

    return len(rooms)


def main() -> None:
    n = int(sys_input())
    time_table = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(time_table)
    print(answer)


if __name__ == "__main__":
    main()