def parseInput(filename):
	
	f = open(filename)

	matrix = []
	row = []
	
	for line in f:
		for row in line.split(";"):
			row = row.strip()
			matrix.append(row.split(","))
		print(isSym(matrix))
		matrix = []
		row = []


def isSym(arrOfArrs):

	rowSize = len(arrOfArrs)
	colSize = len(arrOfArrs[0])

	if rowSize == 1 and colSize == 1:
		return "Symmetric"
	if rowSize != colSize:
		return "Not symmetric"

	for row in range(rowSize):
		for col in range(colSize):
			if(arrOfArrs[row][col] != arrOfArrs[col][row]):
				return "Not symmetric"

	return "Symmetric"
		

parseInput("Matrix-Symmetry_InputForSubmission_1.txt")
