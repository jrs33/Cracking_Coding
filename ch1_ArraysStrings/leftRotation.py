#
# Performing a left rotation on an array
#

def leftRotation(arrayArgs, n):

    temporaryArray = []

    # Storing arrayArgs[0] elements in a temporary array
    # since they shift in from the right
    for i in range(arrayArgs[0]):
        temporaryArray.append(n[i])

    # Shift the remaining elements to the left
    for i in range(arrayArgs[0],len(n)):
        n[i-d] = n[i]

    for i in range(len(n)-arrayArgs[0],len(n)):
        n[i] = temporaryArray[i-(len(n)-arrayArgs[0])]

    for i in range(len(n)):
        print(n[i])
        print(" ")

leftRotation([5,4], [1,2,3,4,5])

#
# Here I take advantage of the pattern of the shifting out of d elements to the
# back of the array. I store the d values in a temp array, shift the current elements
# left by d and then place the d temp elements to the back of the array. In total, we
# have O(length(n)) time and O(d) space complexity, which can be reduced by just doing a
# one by one computation
#
