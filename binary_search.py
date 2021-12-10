from typing import List


def binary_search(arr: List[int], low: int, high: int, x: int) -> int:
    """
    Binary search algorithm.
    """

    while low <= high:
        mid: int = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    return -1


arr_data: List[int] = [6, 15, 22, 44, 50, 65]
count_search: int = 44

result: int = binary_search(arr_data, 0, len(arr_data) - 1, count_search)

if result == -1:
    print('Sorry, not found!')
else:
    print('Found at index:', result)
