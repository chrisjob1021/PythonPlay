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
	def grayCode(self, n):
		solution = [0]

		for i in xrange(n):
			solution += [x + pow(2,i) for x in reversed(solution)]

		for d in solution:
			print "{0:b}".format(d)

		return solution

print Solution().grayCode(2)
print Solution().grayCode(3)

