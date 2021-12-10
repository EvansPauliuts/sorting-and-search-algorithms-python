from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    largest: int = i
    l: int | float = 2 * i + 1
    r: int | float = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> None:
    """
    Heap sort algorithm.
    """

    n: int = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr_data: List[int] = [8, 11, 6, 2, 1, 9]
heap_sort(arr_data)

print(arr_data)
