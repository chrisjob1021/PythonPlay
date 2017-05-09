'''

https://leetcode.com/problems/two-sum/?tab=Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution(object):
	def two_sum(self, number_list, target):
		if len(number_list) <= 1:
			return False

		solutions = { }
		for i in range(len(number_list)):
			if number_list[i] in solutions:
				return [solutions[number_list[i]], i]
			else:
				solutions[target - number_list[i]] = i


#print Solution().two_sum([2, 7, 11, 15], 9)
print Solution().two_sum([6, 13, 14, 16], 22)