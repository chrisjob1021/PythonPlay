class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def hammingDistance(x, y):
        	return

        return reduce(lambda acc, digit: [bin(x^y).count('1') for x in acc for y in nums[digit]], nums)
        

print Solution().totalHammingDistance([4, 14, 2])