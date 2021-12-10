from typing import List


def insertion_sort(arr: List[int]) -> None:
    """
    Insertion sort algorithm.
    """

    for i in range(1, len(arr)):
        key: int = arr[i]
        j: int = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


arr_data: List[int] = [25, 15, 44, 18, 26]
insertion_sort(arr_data)
print(arr_data)
