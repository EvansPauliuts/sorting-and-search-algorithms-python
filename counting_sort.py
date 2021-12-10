from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting sort algorithm.
    """

    min_val: int = min(arr)
    max_val: int = max(arr)

    counts: List[int] = [0] * (max_val - min_val + 1)

    for i in arr:
        counts[i - min_val] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    sorted_arr: List[int] = [0] * len(arr)

    for j in arr[::-1]:
        counts[j - min_val] -= 1
        sorted_arr[counts[j - min_val]] = j

    return sorted_arr


arr_data: List[int] = [2, 1, 0, 3, 8, 3, 3]
print(counting_sort(arr_data))
