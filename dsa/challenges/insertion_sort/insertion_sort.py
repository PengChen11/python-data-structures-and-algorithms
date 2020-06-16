
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        # temp = arr[i]

        while j>= 0 and arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j],arr[j+1]
            j = j-1

        # arr[j+1] = temp
    return arr


if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    test = insertion_sort(arr)
    print(test)
