'''https://discuss.leetcode.com/topic/9815/python-o-n-2-solution'''

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        count = 0
        nums.sort()
        
        for i in xrange(0,n-2):
            l = i+1
            r = n-1
            
            while l < r:
                print i, l, r
                curr = nums[i] + nums[l] + nums[r]
                if curr < target:
                    # After sorting, if i, j, k is a valid triple, then i, j-1, k, ..., i, i+1, k are also valid triples. No need to count them one by one.
                    count += r - l
                    l += 1
                else:
                    r -= 1
            
        return count


print Solution().threeSumSmaller([-2, 0, 1, 3], 2)
