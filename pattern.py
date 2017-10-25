#BCDDCDABCDABCDDDCDA
import re
def pattern(stringIn):

	pattern = "AB.(?=D)"

	match = re.findall(pattern, stringIn)
	print(len(match))

pattern("ABCDDCDABCDABCDDDCDA")
