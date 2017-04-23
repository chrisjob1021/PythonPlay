'''
You are given 2 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at bit i.

You can assume that bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
You would not, for example, have j = 3 and i =2, because M could not fully fit between bit 3 and 2.

Input: N = 10000000000, M = 10011, i = 2, j = 6
Output N = 10001001100
'''

# 1. Clear the bits j through i in N
# 2. Shift M so that it lines up with bits j through i
# 3. Merge M and N
class Solution:
	def printBits(self, num):
		return bin((1 << 11) - 1 & num)
	def insertion(self, n, m, i, j):
		N = int(n, 2)
		M = int(m, 2)

		print self.printBits(N)
		print self.printBits(M)

		allOnes = ~0

		# Comments using i=2, j=4

		# 1s before position j, then 0s
		# left = 11100000
		left = allOnes << (j + 1)

		# 1s after position i
		# right = 00000011
		right = ((1 << i ) - 1)

		# All 1s except for 0s between i and j
		# mask = 11100011
		mask = left | right

		n_cleared = N & mask
		m_shifted = M << i

		return self.printBits(n_cleared | m_shifted)


print Solution().insertion('10000000000', '10011', 2, 6)
