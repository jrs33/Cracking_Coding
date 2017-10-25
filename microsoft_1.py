import string

def dateFormater(original, inPattern, outPattern):

	separator = ""

	# Extracting the separator
	for char in inPattern:
		if not char.isalnum():
			separator = char
			break

	inArr = inPattern.split(separator)
	origArr = original.split(separator)

	pairedDict = dict(zip(inArr,origArr))

	newSeparator = ""
	for char in outPattern:
                if not char.isalnum():
                        newSeparator = char
                        break

	outArr = outPattern.split(newSeparator)
	outString = ""
	for key in outArr:
		outString += pairedDict[key]
		outString += newSeparator

	return outString[:-1]	

def parseInput(filename):

	f = open(filename, 'r')
	
	for line in f:
		(orig, inPat, outPat) = line.split(" ")
		outPat = outPat.strip()
		print(dateFormater(str(orig),str(inPat),str(outPat)))

parseInput("Calendar-confusion_InputForSubmission_1.txt")
