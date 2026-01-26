""" selection_sort.py """

def solve(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n - 1, -1, -1):
        max_idx = i
        for j in range(i):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


def main() -> None:
    arr = [13, 2, 7, 116, 62, 235, 1, 23, 55, 77]

    answer: list[int] = solve(arr)
    print(answer)


if __name__ == "__main__":
    main()
