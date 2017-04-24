'''
You are given 2 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at bit i.

You can assume that bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
You would not, for example, have j = 3 and i =2, because M could not fully fit between bit 3 and 2.

Input: N = 10000000000, M = 10011, i = 2, j = 6
Output N = 10001001100


Note: For i, j, indexing starts at 0
'''

# clear bits between i and j
# move M over
# insert M into N

class Solution:
	def bitInsertion(self, bitsN, bitsM, i, j):
		def printBits(num):
			return '{0:b}'.format(num)

		# convert bits to integers
		n = int(bitsN, 2)
		m = int(bitsM, 2)

		all1s = ~0

		# create mask to clear bits between i and j
		# get left half of mask
		# 11111000000
		left = all1s << (j + 1)

		# get right half of mask
		# 00000000011
		right = (1 << i) - 1

		# combine the two masks
		mask = left | right

		# clear n between i and j using mask
		ncleared = n & mask

		# move m over i bits
		mmoved = m << i

		# insert m into n
		return printBits(n | mmoved)

print Solution().bitInsertion('10000000000', '10011', 2, 6) # expect 10001001100