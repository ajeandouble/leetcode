def partition(low, high):
    pass


def quicksort(arr):
    def qs(low, high):
        if low >= high:
            return

        pivot = arr[high]
        left = low - 1
        for right in range(low, high):
            if pivot < arr[right]:
                left += 1
                arr[left], arr[right] = arr[right], arr[left]
        left += 1
        print(arr[left], pivot)
        arr[left], arr[high] = arr[high], arr[left]
        qs(low, left - 1)
        qs(left + 1, right)

    return qs(0, len(arr) - 1)


nums = [2, 3, -1, 0, 4, 5, 6, -2, -3]
ret = quicksort(nums)
print(f"ret = {nums}")
