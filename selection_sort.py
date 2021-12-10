from typing import List


def selection_sort(arr: List[int]) -> None:
    """
    Selection sort algorithm
    """

    for i in range(len(arr)):
        min_index: int = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr_data: List[int] = [6, 25, 34, 14, 50, 4]
selection_sort(arr_data)
print(arr_data)
