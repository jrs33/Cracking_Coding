#
# Implement an algorithm to determine if a string has all unique characters
#

def isUnique(stringArgument, numCharacters):

    # Mini optimization; if the length of the string is greater than the number of characters,
    # it cannot possibly be unique
    if(len(stringArgument) > numCharacters):
        return False
    else:
        # Creating a hash map to map ASCII.value ->
        characterSet = [False] * numCharacters

        # Iterate through the length of the string and map values
        # to the indeces of the array
        for i in range(len(stringArgument)):
            # Convert from ASCII to integer equivalent
            value = ord(stringArgument[i])

            if(characterSet[value]):
                return False
            else:
                characterSet[value] = True

    return True

# Assuming extended ASCII which has 256 total characters
print(isUnique(['j','o','s','h'], 256))


#
# Will run in O(c) amortized time where c is the number of characters in the encoding
# (ie: ASCII, Unicode, etc.). O(c) space complexity as well from the hash map
#
