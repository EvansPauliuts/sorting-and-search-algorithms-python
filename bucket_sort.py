from typing import List


def bucket_sort(arr: List[int]) -> List[int]:
    """
    Bucket sort algorithm
    """

    max_element: int = max(arr)
    n: int = len(arr)
    size: int | float = max_element / n

    buckets = [[] for _ in range(n)]

    for i in range(n):
        index: int | float = int(arr[i] / size)

        if index != n:
            buckets[index].append(arr[i])
        else:
            buckets[n - 1].append(arr[i])

    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    result: List[int] = []
    for i in range(n):
        result = result + buckets[i]

    return result


arr_data: List[int] = [10, 6, 2, 5, 9, 4]
print(bucket_sort(arr_data))
