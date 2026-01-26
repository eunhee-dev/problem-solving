""" quick_sort.py """

def quick_sort(arr: list[int], start: int, end: int):
    if end <= start + 1:
        return

    pivot = arr[start]
    l, r = start + 1, end - 1

    while True:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and arr[r] >= pivot:
            r -= 1
        if l > r:
            break
        arr[l], arr[r] = arr[r], arr[l]

    arr[start], arr[r] = arr[r], arr[start]
    quick_sort(arr, start, r)
    quick_sort(arr, r + 1, end)


def solve(arr: list[int]) -> list[int]:
    quick_sort(arr, 0, len(arr))
    return arr


def main() -> None:
    arr = [13, 2, 7, 116, 62, 235, 1, 23, 55, 77]

    answer: list[int] = solve(arr)
    print(answer)


if __name__ == "__main__":
    main()
