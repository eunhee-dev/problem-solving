""" merge_sort.py """

def merge(a: list[int], b: list[int]) -> list[int]:
    c = []
    a_i, b_i = 0, 0

    while a_i < len(a) and b_i < len(b):
        if a[a_i] <= b[b_i]:
            c.append(a[a_i])
            a_i += 1
        else:
            c.append(b[b_i])
            b_i += 1

    c.extend(a[a_i:])
    c.extend(b[b_i:])
    return c


def solve(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    merged_arr = []

    mid = len(arr) // 2
    left_half = solve(arr[:mid])
    right_half = solve(arr[mid:])

    merged_arr.extend(merge(left_half, right_half))
    return merged_arr


def main() -> None:
    arr = [13, 2, 7, 116, 62, 235, 1, 23, 55, 77]

    answer: list[int] = solve(arr)
    print(answer)


if __name__ == "__main__":
    main()
