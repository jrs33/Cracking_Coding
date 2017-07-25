#
# Gets the next largest number with equal 1 bits
#

def getNext(inputNum):

	binVal = bin(inputNum)

	binArr = [int(char) for char in binVal[2::]]

	# Ex : 10110110 -> 10111001
	#
	# Here we want to find the rightmost leading zero
	# to avoid drastically increasing the number
	rightMostInd = 0
	lastVal = 0
	for bit in range(0, len(binArr)-1):
		if(binArr[bit] == 0 and binArr[bit+1] == 1 and bit > rightMostInd):
			rightMostInd = bit
	print(rightMostInd)
	# Recording the number of 1's in the number
	oneCount = 0
	for i in range(0, len(binArr)):
		if(binArr[i] == 1):	
			oneCount = oneCount + 1
	
	# Clearing the bits to the right of the rightmost index
	indexShift = 1 << rightMostInd
	negMask = indexShift - 1
	mask = ~negMask
	inputNum = inputNum & mask

	# Adding in the oneCount-1 1's 
	starter = 1 << oneCount-1 
	starterNeg = starter - 1
	inputNum = inputNum | starterNeg
	
	print(inputNum)
	return inputNum

getNext(22)
