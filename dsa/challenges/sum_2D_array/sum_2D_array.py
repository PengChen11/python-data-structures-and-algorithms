# guess I can't use list.append()

def sum_2D_array(inputMatrix):
    outputArray=[0]*len(inputMatrix)
    for i in range(len(inputMatrix)):
        sum = 0
        for a in range(len(inputMatrix[i])):
            sum += inputMatrix[i][a]
        outputArray[i]=sum
    return outputArray

