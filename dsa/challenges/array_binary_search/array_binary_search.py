# Here's the binary search function.
def BinarySearch(inputArray, key):
    # since we are searching from a sorted array, if the key is greater than the last element inside of the array, don't even do the search. just return -1.
    if inputArray[len(inputArray)-1]<key:
        return -1
    else:
        # then will always compair the key with element that has the middle index first, if key is smaller than that element, get rid or the greater half of the array, do the search again; vice versa.
        start=0
        end=len(inputArray)-1
        while start<=end:
            mid=(start+end)//2
            if inputArray[mid]==key:
                return mid
            else:
                if key<inputArray[mid]:
                    end = mid-1
                else:
                    start = mid+1
    return -1


if __name__ == "__main__":
    from textwrap import dedent

    print(dedent("""
    ***************************************
    ** Please input a sorted array,      **
    ** seperate by space. no [ ] needed. **
    ** e.g.   1 2 3 4 5 6                **
    ***************************************
    """))
    inputArray = [int(elem) for elem in input().split()]

    print(dedent("""
    *******************************************************
    ** Please input the key to be searched in that array **
    *******************************************************
    """))

    key = int(input())
    result = BinarySearch(inputArray, key)
    if result != -1:
        print('The index for the element matching that key is:', result)
    else:
        print('There is no element matching that key inside the array')

