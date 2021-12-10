from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    pivot: int = arr[high]
    i: int = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: List[int], low: int, high: int) -> None:
    """
    Quick sort algorithm.
    """

    if len(arr) == 1:
        return arr

    if low < high:
        pi: int | float = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr_data: List[int] = [15, 64, 6, 52, 18, 20]
length_arr: int = len(arr_data)
quick_sort(arr_data, 0, length_arr - 1)
print(arr_data)
