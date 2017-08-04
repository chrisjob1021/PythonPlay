class Solution(object):
    def findDuplicate(self, nums):
        slow = fast = finder = 1
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder

print Solution().findDuplicate([5,3,8,2,9,3,4,11])