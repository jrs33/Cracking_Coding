from collections import OrderedDict

def parseInput(filename):

	f = open(filename)

	messageArr = []
	for line in f:
		messageArr.append(line.strip())

	resolveMessages(messageArr)

def resolveMessages(strArray):

	print("Here")
	messageData = dict()
	for string in strArray:
		if(messageData[string]):
			messageData[string] += 1
		else:
			messageData.update(dict(string=1))

	print(messageData)

parseInput("PracticeInput.txt")
