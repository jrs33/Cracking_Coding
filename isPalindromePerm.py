#
# Given a string, determine whether the result is a permutation of a palindrome
#

def isPalindromePerm(str):

    # Assuming the string is not case sensitive (ie: only has values a-z)
    # we start by building a hash map to map character values to an index
    # which stores the number of those characters present
    charFrequencyMap = [0] * (ord('z') - ord('a'))

    for i in range(len(str)):

        charFrequencyMap[ord(str[i]) - ord('a')] = charFrequencyMap[ord(str[i]) - ord('a')] + 1


    oddCount = 0

    for i in range(len(charFrequencyMap)):

        # Check to see if there are any odd numbers of characters, and if there
        # are more than 2 instances of odd characters, we do not have a palindrome permutation
        if(oddCount > 1):
            return False
        if(charFrequencyMap[i] % 2 != 0):
            oddCount = oddCount + 1

    return True

print(isPalindromePerm("tactcoa"))

#
# The time complexity here is O(n) where n is the length of the string, taking
# advantage of using a hash map and pattern recognition to reduce computation time
#
