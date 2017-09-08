class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + path for i, n in enumerate(nums) for path in self.permute(nums[:i] + nums[i+1:])] or [[]]

print Solution().permute([1,1,2])