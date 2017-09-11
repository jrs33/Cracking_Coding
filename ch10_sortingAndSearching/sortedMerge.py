def sortedMerge(arrayA, arrayB):

	endA = len(arrayA) - 1
	endB = len(arrayB) - 1
	endMerge = len(arrayA) + len(arrayB) - 1

	while(endB >= 0):
		if(arrayA[endA] > arrayB[endB]):
			arrayA[endMerge] = arrayA[endA]
			endA -= 1
		elif(arrayA[endA] < arrayB[endB]):
			arrayA[endMerge] = arrayB[endB]
			endB -= 1
		endMerge -= 1


sortedMerge([1,4,7], [2,5,9])	
