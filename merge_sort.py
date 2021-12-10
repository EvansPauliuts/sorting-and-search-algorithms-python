from typing import List


def merge_sort(arr: List[int]) -> None:
    """
    Merge sort algorithm
    """

    if len(arr) > 1:
        mid: int = len(arr) // 2
        left: int = arr[:mid]
        right: int = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr_data: List[int] = [25, 6, 34, 90, 15]
merge_sort(arr_data)
print(arr_data)
