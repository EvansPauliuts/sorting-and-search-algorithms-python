from typing import List


def counting_sort(arr: List[int], place: int) -> None:
    size: int = len(arr)
    output: List[int] = [0] * size
    count: List[int] = [0] * 10

    for i in range(0, size):
        idx: int = arr[i] // place
        count[idx % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        idx: int = arr[i] // place
        output[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix sort is a non-comparative integer sorting algorithm.
    It sorts items by grouping keys that are the same integer
    length into buckets.
    """

    max_element: int = max(arr)
    place: int = 1

    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10


arr_data: List[int] = [100, 201, 1, 810, 904, 6, 25]
radix_sort(arr_data)
print(arr_data)
