#
# Write method given two strings to identify if one is a permutation of the other
#

def isPermutation(stringOne, stringTwo, encodingNums):

    # Assuming the strings are case sensitive

    if(len(stringOne) != len(stringTwo)):
        return False

    # Creates hash map to map encoded int values to indeces
    stringMap = [False] * encodingNums

    # Iterate through the first string and use an array as a hash map
    for i in range(len(stringOne)):
        stringMap[ord(stringOne[i])] = True

    for i in range(len(stringTwo)):
        if(stringMap[ord(stringTwo[i])] == False):
            return False

    return True

print(isPermutation(['a','b','c'],['b','c','s','s'],128))
print(isPermutation(['a','b','c'],['b','c','a'],128))

#
# Here we have an amortized runtime from the optimization of length checks of O(n)
# where n is the length of the strings. The space complexity is O(encodingNums) which
# denotes the possible number of characters in the encoding specified
#
