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
	# DFS recursively 
	def subsets(self, nums):
	    def dfs(index, path):
	        res.append(path)
	        for i in xrange(index, len(nums)):
	            # recursively call dfs incrementing index and building path with number of digits according to xrange
	            dfs(i+1, path+[nums[i]])
	    res = []
	    # call dfs with index at 0 and path empty
	    dfs(0, [])
	    return res
	    
print Solution().subsets([1,2,3])