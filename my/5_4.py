'''
Next Number: Given a positive integer, print the next smallest and the next largest number that have the same. number of 1 bits in their binary representation
'''

class Solution:
	def nextNumbers(self, num):
		def printBits(num):
			print '{0:b}'.format(((1 << 15) - 1 & num)).zfill(15)


		def getNext(num):
			# identify trailing 0s (c0)
			# identify sequence of 1s after 0s (c1)
			# flip bit at c0 + c1 (p)
			# excluding p, clear p > end
			# add c1-1 1s back in 

			n = num
			c0 = c1 = 0

			while (n & 1) == 0 and n != 0:
				c0 += 1
				n = n >> 1

			while (n & 1) == 1:
				c1 += 1
				n = n >> 1

			p = c0 + c1

			# no bigger number with same number of 1s if p == 31
			if p == 31 or p == 0: # can't keep same number of bits if our number is 0
				return -1

			printBits(num)
			print p, c0, c1

			num |= (1 << p)	# flip bit @ bit
			printBits(num)
			num &= (~0 << p)
			printBits(num)
									# 11011001110000
									# 11111111000000

									# 11011001000000
									# 00000000001111
									# (1 < c1) - 1 
			num |= (1 << c1 -1 )-1
			printBits(num)
			return num

		return getNext(num)

print Solution().nextNumbers(13948) # next = 13967
#print Solution().nextNumbers(10115) # prev = 10096
