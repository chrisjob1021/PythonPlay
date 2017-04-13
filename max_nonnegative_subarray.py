'''
https://www.interviewbit.com/problems/max-non-negative-subarray/?ref=success-next-suggestion

Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index

'''

class Solution:
    # Space: O(n)
    # Time: O(n)

    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
    	if len(A) == 0:
    		return []

        def addSol(sol):
            if len(sol) > 0:
                solL.append(sol)

        # Space: O(n)
        solL = [ ]
        sol = [ ]
        # Time: O(n)
        for i in xrange(len(A)):
            if A[i] >= 0:
                sol.append(A[i])
            else:
                addSol(sol)
                sol = [ ]
                continue

        addSol(sol)

        # Space: O(n)
        solD = {}

        # Time: O(n)
        for i in xrange(len(solL)):
            sumSub = sum(solL[i])
            if sumSub in solD:
                solA, solB = solL[i], solD[sumSub]
                if len(solA) > len(solB):
                    solD[sumSub] = solL[i]
                elif len(solA) == len(solB):
                    if solA[0] < solB[0]:
                        solD[sumSub] = solL[i]
            else:
                solD[sumSub] = solL[i]

        if len(solD) > 0:
            return solD[max(solD.keys())]
        else:
            return []


print Solution().maxset([1, 2, 5, -7, 2, 3])
print Solution().maxset([-1, -1, -1, -7, -1, -1])
print Solution().maxset([1, 2, 5])
print Solution().maxset([756898537, -1973594324, -2038664370, -184803526, 1424268980])
print Solution().maxset([ 0, 0, -1, 0 ])