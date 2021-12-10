from typing import List


def linear_search(arr: List[int], n: int, x: int) -> int:
    """
    Linear search algorithm.
    """

    for i in range(0, n):
        if arr[i] == x:
            return i

    return -1


arr_data: List[int] = [4, 10, 20, 8, 15, 6]
count_search: int = 8
length_arr: int = len(arr_data)

result: int = linear_search(arr_data, length_arr, count_search)

if result == -1:
    print('Sorry, not found!')
else:
    print('Found at index:', result)
