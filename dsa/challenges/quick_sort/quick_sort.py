
def quick_sort(arr, left=0, right=None):
    '''function to do the array quick sort'''
    if right is None:
        right = len(arr)-1
    if left < right:
        position = partition(arr,left,right)
        quick_sort(arr, left, position-1 )
        quick_sort(arr, position+1, right)

def partition(arr, left, right):
    '''function to seperate the array into two piece by the value of the last element, and return the position in modified array'''
    pivot = arr[right]
    low = left-1
    for i in range(left, right):
        if arr[i]<= pivot:
            low +=1
            arr[i],arr[low]=arr[low],arr[i]

    arr[right],arr[low+1]=arr[low+1],arr[right]

    return low+1


if __name__ == "__main__":
    test = [8,23,23,42,16,15]
    quick_sort(test)
    print(test)
