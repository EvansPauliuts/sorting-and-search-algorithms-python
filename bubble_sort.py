from typing import List


def bubble_sort(arr: List[int]) -> None:
    """
    Bubble sort algorithm
    """

    n: int = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr_data: List[int] = [15, 99, 44, 18, 26, 6]
bubble_sort(arr_data)
print(arr_data)
