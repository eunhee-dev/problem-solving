""" bubble_sort.py """

def solve(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main() -> None:
    arr = [-2, 2, 4, 6, 13]

    answer: list[int] = solve(arr)
    print(answer)


if __name__ == "__main__":
    main()
