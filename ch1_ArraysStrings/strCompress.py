#
# Perform basic string compression using the counts of repeated characters
#
# aabb -> a2b2
#

def strCompress(str):

        # Use a mutable array to avoid extra time needed to copy
        # characters over for concatenation, which would be a copy
        # character by character into a new string which is
        # exponential
        compressedString = list()
        consecCount = 1

        for i in range(len(str)):

            if(i == 0):

                compressedString.append(str[0])

            else:

                if(str[i] == str[i-1]):
                    # Handling special case where last character section is a subset
                    if(i == len(str) - 1):
                        consecCount = consecCount + 1
                        compressedString.append(consecCount)
                    # Incrementing the consecCount if we have a set of equal chars
                    else:
                        consecCount = consecCount + 1

                # If we break a sequence, we append the count and new character and reset
                # the consecCount
                else:
                    compressedString.append(consecCount)
                    compressedString.append(str[i])
                    consecCount = 1

        # Double checking to see if the compressed string is shorter than the original before printing
        if(len(compressedString) < len(list(str))):
            return compressedString
        else:
            return list(str)

print(strCompress("aaabaaaaaffass")) # -> ['a', 3, 'b', 1, 'a', 5, 'f', 2, 'a', 1, 's', 2]
print(strCompress("abcdefg")) # -> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#
# The time complexity here is simply O(n) where n is the length of the passed
# string. The important optimization here is using a resizeable array to avoid
# copying chars, which costs a O(n + 2n + 3n .... n^2) complexity. The time complexity
# here is at most O(n) since we will either store the original string or a compressed version
#
