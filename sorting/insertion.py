from typing import Optional, List

def insertion_sort(arr: List[int]) -> List[int]:
    N = len(arr)
    for i in range (0, N):
        j = i - 1
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

    return arr

assert insertion_sort([2,3,4,1,6]) == [1,2,3,4,6]
assert insertion_sort([1]) == [1]
assert insertion_sort([2,1]) == [1,2]
assert insertion_sort([2,1,3]) == [1,2,3]
assert insertion_sort([-2,1,3]) == [-2,1,3]
