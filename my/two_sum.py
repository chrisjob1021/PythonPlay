'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
	def twoSum(self, target, nums):
		if len(nums) <= 1:
			return False

		solution = { }

		for i in xrange(len(nums)):
			if nums[i] in solution:
				return [solution[nums[i]], i]
			else:
				solution[target - nums[i]] = i

		return False

print Solution().twoSum(9, [2, 7, 11, 15])

print Solution().twoSum(26, [2, 7, 11, 15])

print Solution().twoSum(22, [6, 13, 14, 16])

print Solution().twoSum(25, [6, 13, 14, 16])