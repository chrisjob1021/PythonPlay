'''
https://leetcode.com/problems/subsets/?tab=Description#/description

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution(object):
	def subsets(self, nums):
		solution = [ ]
		n = len(nums)

		def sub(index, path):
			solution.append(path)

			for i in xrange(index,n):
				sub(i+1,path+[nums[i]])

		sub(0,[])

		return solution

print Solution().subsets([1,2,3])
