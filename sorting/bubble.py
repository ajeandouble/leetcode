from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    N = len(arr)
    for i in range(0, N):
        for j in range(0, N - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

assert bubble_sort([1]) == [1]
assert bubble_sort([1,2]) == [1,2]
assert bubble_sort([2,1]) == [1,2]
assert bubble_sort([2,1,3]) == [1,2,3]
assert bubble_sort([-1,-1,3]) == [-1,-1,3]
assert bubble_sort([]) == []