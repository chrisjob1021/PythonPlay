'''
https://leetcode.com/problems/kth-largest-element-in-an-array/?tab=Description

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <= array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

import heapq

class Solution(object):
	# O(nlgn) time
	def findKthLargest1(self, nums, k):
	    return sorted(nums, reverse=True)[k-1]

	# O(nk) time, bubble sort idea, TLE
	def findKthLargest2(self, nums, k):
	    for i in xrange(k):
	        print "i: %d" % i
	        for j in xrange(len(nums)-i-1):
	            print "len(nums): %d - nums[j]: %d - 1" % (len(nums), nums[j])
	            if nums[j] > nums[j+1]:
	                # exchange elements, time consuming

	                nums[j], nums[j+1] = nums[j+1], nums[j]
	    print nums
	    return nums[len(nums)-k]

	# O(nk) time, selection sort idea
	def findKthLargest3(self, nums, k):
	    for i in xrange(len(nums), len(nums)-k, -1):
	        print "i: %d" % i
	        tmp = 0
	        for j in xrange(i):
	            print nums
	            print "j: %d if nums[j]: %d > nums[tmp]: %d " % (j, nums[j], nums[tmp])
	            if nums[j] > nums[tmp]:
	                tmp = j
	        print "i: %d (-1) tmp: %d" % (i, tmp)
	        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
	        print nums
	    print "nums[len(nums)-k] %d" % nums[len(nums)-k]
	    return nums[len(nums)-k]

	# O(k+(n-k)lgk) time, min-heap
	def findKthLargest4(self, nums, k):
	    heap = []
	    for num in nums:
	        heapq.heappush(heap, num)
	    for _ in xrange(len(nums)-k):
	        heapq.heappop(heap)
	    return heapq.heappop(heap)

	# O(k+(n-k)lgk) time, min-heap        
	def findKthLargest5(self, nums, k):
	    return heapq.nlargest(k, nums)[k-1]

	def findKthSmallest(self, nums, k):
	    if nums:
	        pos = self.partition(nums, 0, len(nums)-1)
	        print "pos: %d" % pos
	        if k > pos+1:
	            print "HERE nums[pos+1:]: " + str(nums[pos+1:])
	            return self.findKthSmallest(nums[pos+1:], k-pos-1)
	        elif k < pos+1:
	            print "HERE nums[:pos]: " + str(nums[:pos])
	            return self.findKthSmallest(nums[:pos], k)
	        else:
	            return nums[pos]

	# O(n) time, quick selection
	def findKthLargest(self, nums, k):
	    # convert the kth largest to smallest
	    return self.findKthSmallest(nums, len(nums)+1-k)

	# choose the right-most element as pivot   
	def partition(self, nums, l, r):
	    print "partition"
	    low = l
	    print "l: %d r: %d" % (l, r)
	    print "initial nums: " + str(nums)
	    while l < r:
	        print "if nums[l] %d < nums[r] %d" % (nums[l], nums[r])
	        if nums[l] < nums[r]:
	            print "set nums[l] %d to nums[low] %d and vice versa" % (nums[l], nums[low])
	            nums[l], nums[low] = nums[low], nums[l]
	            low += 1
	            print "new nums: " + str(nums)
	        l += 1
	    print "set nums[low] %d to nums[r] %d and vice versa" % (nums[low], nums[r])
	    nums[low], nums[r] = nums[r], nums[low]
	    print "final nums: " + str(nums)
	    return low


print Solution().findKthLargest([3,2,1,5,6,4], 2)