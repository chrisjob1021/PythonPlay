class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        candidate1, candidate2, counter1, counter2 = 0, 1, 0, 0

        for num in nums:
            if num == candidate1:
                counter1 += 1
            elif num == candidate2:
                counter2 += 1
            elif counter1 == 0:
                candidate1 = num
                counter1 = 1
            elif counter2 == 0:
                candidate2 = num
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1

        return candidate1, candidate2
    
print Solution().majorityElement([1])

            


