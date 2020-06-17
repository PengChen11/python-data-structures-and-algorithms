def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        if i == len(left):
            arr[k:]=right[j:]

        else:
            arr[k:]=left[i:]


if __name__ == "__main__":
    test1 = [8,7,6,5,4,3,2,1]
    test2 = [8,4,23,42,16,15]
    test3 = [5,12,7,5,5,7]
    merge_sort(test1)
    merge_sort(test2)
    merge_sort(test3)
    print(test1)
    print(test2)
    print(test3)
