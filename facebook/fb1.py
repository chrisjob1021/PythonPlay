'''
# Given an array of integers greater than zero, find if it is possible to 
# split it in two (without reordering the elements), such that the sum
# of the two resulting arrays is the same. Print the resulting arrays.

[2, 3, 2, 1, 1, 1, 2, 1, 1] ==> [2, 3, 2], [1, 1, 1, 2, 1, 1]

[7], [1, 1, 1, 2, 1, 1]
'''

class Solution(object):
	def sumArrays(self, nums):
		n = len(nums)

		for i in xrange(1,n):
			if sum(nums[0:i]) == sum(nums[i:n]):
				return [nums[0:i], nums[i+1:n]]

		return [ ]


print Solution().sumArrays([2, 3, 2, 1, 1, 1, 2, 1, 1])
print Solution().sumArrays([7, 1, 1, 1, 2, 1, 1])