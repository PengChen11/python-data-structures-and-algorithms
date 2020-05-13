# if I can't use any build-in array method
def insertShiftArray(inputArray, num):
  newArray=[0]*(len(inputArray)+1)
  for i in range(len(inputArray)):
    if i <(len(inputArray)+1)//2:
      newArray[i]=inputArray[i]
    elif i == (len(inputArray)+1)//2:
      newArray[i]=num
      newArray[i+1]=inputArray[i]
    else:
      newArray[i+1]=inputArray[i]
  return newArray


# if I can use list.append method
def insertShiftArray2(inputArray, num):
  newArray=[]
  for i in range(len(inputArray)):
    if i==(len(inputArray)+1)//2:
      newArray.append(num)
      newArray.append(inputArray[i])
    else:
      newArray.append(inputArray[i])
  return newArray


#Here's the stretch goal to remove the element with middle index from input array
# it is not using any build-in list method
def removeShiftArray(inputArray):
  newArray = [0]*(len(inputArray)-1)
  for i in range(len(inputArray)):
    if i <(len(inputArray))//2:
      newArray[i]=inputArray[i]
    elif i == (len(inputArray))//2:
      continue
    else:
      newArray[i-1]=inputArray[i]
  return newArray


if __name__ == "__main__":
    from textwrap import dedent
    print(dedent("""
    ***************************************
    ** Please input an array,            **
    ** seperate by space. no [ ] needed. **
    ** e.g.   1 2 3 4 5 6                **
    ***************************************
    """))
    inputArray = [int(elem) for elem in input().split()]

    print(dedent("""
    *******************************************************
    ** Please input the number to be added to that array **
    *******************************************************
    """))

    key = int(input())
    result = insertShiftArray(inputArray, key)

    print('The modified Array is','\n', *result)
