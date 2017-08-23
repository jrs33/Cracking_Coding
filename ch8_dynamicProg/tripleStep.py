# A non-memoized version
def stepCount(n):
	
	if n < 0:
		
		return 0	

	elif n == 0:

		return 1

	else:

		return stepCount(n-1)+stepCount(n-2)+stepCount(n-3)

# This is the memoized cache example which runs in O(n) rather than O(3^n) as shown above
def optimizedStepCount(n):
	
	# Create an n length List of zeroes (ie: [0,0,0,0] for n=4)
	newCache = [0] * n
	memoStep(n, newCache)

def memoStep(n, cache):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif cache[n] == 0: #specific step data has not been cached
		cache[n] = memoStep(n-1, cache) + memoStep(n-2, cache) + memoStep(n-3, cache)
		return cache[n]
	else:
		return cache[n]
