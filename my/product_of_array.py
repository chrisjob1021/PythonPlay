'''
https://leetcode.com/problems/product-of-array-except-self/?tab=Description

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''

class Solution(object):
	def productOfArray(self, nums):
		solution = [ ]
		n = len(nums)

		p=1
		for i in xrange(n):
			solution.append(p)
			p = nums[i] * p

		p=1
		for i in xrange(n-1,-1,-1):
			solution[i] = solution[i] * p
			p = nums[i] * p

		return solution

print Solution().productOfArray([1,2,3,4]) # [24,12,8,6]
print Solution().productOfArray([2,3,4,5]) # [60, 40, 30, 24]
