import numpy as np

def pathExistsFromOriginToBotRight(grid):

	if(grid == null or len(grid) == 0 or len(grid.T) == 0): return False
	cache = np.matrix([False]*final_r, [False]*final_c)
	roboStep(grid, 0, 0, len(grid), len(grid.T), cache) // Start from origin

def roboStep(grid, r, c, final_r, final_c, cachedPoints):

	// Checks for case of stepping off the board or landing on point that is false
	if(r > final_r or c > final_c or grid[r][c] == False):
		return False

	// Checks to see if there is no path from current node
	if(grid[r][c+1] == False and grid[r+1][c] == False):
		return False

	// Adds dynamic programming element since we wont check the paths from a point we have already visited
	elif(cachedPoints[r][c] == True):
		return False
	
	// Takes two steps and caches point so we wont visit it again for other paths
	elif((r==final_r or c==final_c) 
		or roboStep(grid, r, c+1, final_r, final_c, cachedPoints) 
		or roboStep(grid, r+1, c, final_r, final_c, cachedPoints)
	):
			
		cachedPoints[r][c] = True
		return True

	else:
		print("UNEXPECTED CASE REACHED")
		return False


# We can complete this in O(rn) time rather than exponential with the cache point addition	
