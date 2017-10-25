mapDict = {'A': 1, 'B': 13, 'C': 110}

def stringNum(inputString,mapDict):

	arr = list(inputString)
	runningSum = 0
	runningSubtraction = 0
	currentValue = 0

	for index,char in enumerate(arr):
		print(runningSum)
		print(runningSubtraction)
		if index == 0:
			runningSum += mapDict[arr[index]]
			runningSubtraction -= mapDict[arr[index]]
		elif index == len(arr)-1:
			currentValue += mapDict[arr[index]]
			break
		else:	
			if mapDict[arr[index]] < mapDict[arr[index-1]]:
				runningSubtraction -= mapDict[arr[index]]
				runningSum += mapDict[arr[index]]
				currentValue = runningSum
			elif mapDict[arr[index]] > mapDict[arr[index-1]]:
				runningSubtraction -= mapDict[arr[index]]
                        	runningSum += mapDict[arr[index]]
                        	currentValue = runningSubtraction

	print(currentValue)
	return currentValue

stringNum('CBA',mapDict)
