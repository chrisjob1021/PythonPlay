'''
https://www.interviewbit.com/problems/min-steps-in-infinite-grid/?ref=dash-reco

You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''

class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
    	steps = 0
    	n = len(X)
    	if n == 0:
    		return ret

    	curr = [X[0], Y[0]]

    	for i in xrange(1,n):
    		stepsX = abs(curr[0] - X[i])
    		stepsY = abs(curr[1] - Y[i])
    		steps += max(stepsX, stepsY)
    		curr = [X[i], Y[i]]

    	return steps

print Solution().coverPoints([0,1,1], [0,1,2])