import heapq

class Solution(object):
	def findKthLargest(self, nums, k):
		print nums
		return sorted(nums, reverse=True)[k-1]
	def minHeapFindKthLargest(self, nums, k):
		return heapq.nlargest(k, nums)[k-1]


print Solution().findKthLargest([3,2,1,5,6,4], 2)
print Solution().minHeapFindKthLargest([3,2,1,5,6,4], 2)
