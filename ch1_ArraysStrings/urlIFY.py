#
# Replaces all spaces in a string with '%20' in place
#

def urlIFY(charArray, trueLength):

    # First start by iterating through the array and keeping a count of
    # how many characters we will need in the resulting array
    count = 0

    # In Python, we turn a string into a list for it to be mutable
    charArray = list(charArray)

    print(charArray)

    for i in range(trueLength):
        if(charArray[i] == ' '):
            count = count + 3
        else:
            count = count + 1

    # With this count we can now in-place transform the array by reverse iterating
    # since we have the end buffer to prevent SegFaults. If we run into a space, we
    # replace with the %20 sequence, otherwise we copy the character
    for i in reversed(range(trueLength)):
        if(charArray[i] == ' '):
            charArray[count-1] = '0'
            charArray[count-2] = '2'
            charArray[count-3] = '%'
            count = count - 3
        else:
            charArray[count-1] = charArray[i]
            count = count - 1

    print(charArray)

urlIFY("Mr John Smith    ", 13)

#
# The runtime here is simply O(trueLength)
#
