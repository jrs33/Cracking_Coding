# 
# With a given integer, flip a bit from 0 to a 1, and find longest sequence of 1's
# 

def flipBitToWin(inputNum):
	binaryString = bin(inputNum)

	bitArr = [int(char) for char in binaryString[2::]]
	
	preCount = 0
	postCount = 0
	best = 0
	for bit in bitArr:
		# Haven't encountered a zero yet
		if(bit == 1 and postCount == 0):
			preCount = preCount + 1 
		# Reaching our first zero
		elif(bit == 0 and postCount == 0):
			postCount = postCount + 1
		# Keeping track of post-zero sequence
		elif(bit == 1 and postCount != 0):
			postCount = postCount + 1
		# Encountered the end of that sequence
		elif(bit == 0 and postCount != 0):
			if(preCount + postCount > best):
				best = preCount + postCount
			preCount = postCount - 1
			postCount = 1			
	
	if(preCount + postCount > best):
		best = preCount + postCount
	print(best)
	return best

flipBitToWin(1775)

#
# This algortithm is able to find the largest sequence of 1 bits, given a potential 0->1 flip,
# in O(N) time where N is the length of the resulting binary number
#
