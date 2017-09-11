# Creates keys by sorting strings in alphabetical order; anagrams will be the same when sorted
def sorter(str): 
	b = sorted(str)
	''.join(b)

# Takes in an array of strings and performs a Bucket Sort variant
def grouper(arr):
	anag_dict = {}
	for str in arr:
		key = sorter(str)
		anag_dict.set_default(key, []).append(str)

	groupedArr = []
	for keys,values in anag_dict.items():
		groupedArr.append(values)
