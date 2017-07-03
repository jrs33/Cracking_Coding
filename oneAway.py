#
# Function to check if a string is one letter away from an insert, removal or
# a replacement
#

def isInsertOrRemove(longString, shortString):

    # Pattern searches through each, and then once we reach a difference,
    # we iterate through the larger string once and then continue
    # if we continue to have equal character by character comparisons
    lIterator = 0
    sIterator = 0

    lastWasDifferent = False

    for i in range(len(longString)):
        if(longString[lIterator] == shortString[sIterator]):
            lIterator = lIterator + 1
            sIterator = sIterator + 1
        else:
            if(lastWasDifferent):
                return False
            else:
                lastWasDifferent = True
                lIterator = lIterator + 1

    return True

def isReplaced(oneString, twoString):

    for i in range(len(oneString)):
        

def oneAway(oneString, twoString):

    # Check for all of the different cases to see how to pass the strings
    # to the external one away function checks
    boolResult = False

    if(len(oneString) - len(twoString) == 1):
        boolResult = isInsertOrRemove(oneString, twoString)
    elif(len(twoString) - len(oneString) == 1):
        boolResult = isInsertOrRemove(twoString, oneString)
    elif(len(oneString) == len(twoString)):
        boolResult = isReplaced(oneString, twoString)
    else:
        return False

    return boolResult

print(oneAway("pale","ple"))
