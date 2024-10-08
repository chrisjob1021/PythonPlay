'''
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 
So, in example case, you will return [2, 1, 4, 3] 
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
    	n = len(A)
    	A.sort()

    	#sol = [ ]
    	for i in xrange(0,n,2):
    		if i+1 < n:
    			A[i], A[i+1] = A[i+1], A[i]
    			#sol.append(A[i+1])
    		#sol.append(A[i])

    	return A

print Solution().wave([1, 2, 3, 4])
print Solution().wave([ 5, 1, 3, 2, 4 ])