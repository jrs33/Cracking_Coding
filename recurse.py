def returnTester(x):

	if(x > 5):
		return 2+returnTester(x-1)
	else:
		return 0

print(returnTester(10))
