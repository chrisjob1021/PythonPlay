class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = { }
        n = len(nums)
        res = 0
        for num in nums:
            if num not in d:
                l = d.get(num-1, 0)
                r = d.get(num+1, 0)
                
                curL = l + r + 1
                d[num] = curL
                
                res = max(curL, res)
                
                d[num - l] = curL
                d[num + r] = curL
        print d
        return res

print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])