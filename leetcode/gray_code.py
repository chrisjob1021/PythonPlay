'''
https://leetcode.com/problems/gray-code/?tab=Description

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

'''

class Solution(object):
    # @return a list of integers
    '''
    from up to down, then left to right
    
    0   1   11  110
            10  111
                101
                100
                
    start:      [0]
    i = 0:      [0, 1]
    i = 1:      [0, 1, 3, 2]
    i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
    '''
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results

print Solution().grayCode(2)

# n = 2

# i
# 0: 0 + 1 (0, 1)
# 1: 0 + 2 (0, 1, 2)
# 1: 1 + 2 (0, 1, 2, 3)

