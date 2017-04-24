def printBits(num):
	print '{0:b}'.format((1 << 14) - 1 & num).zfill(14)


'''
p = 7
a = 1 << p # all zeroes except for a 1 at position p
print printBits(a)
b = a - 1 # 0s followed by p 1s
print printBits(b)
mask = ~b # 1s followed by p 0s
print printBits(mask)
# n = n & mask # clears rightmost p bits

print

c1 = 5
a = 1 << (c1 - 1) # 0s with a 1 at position c1-1
print printBits(a)
b = a - 1 # 1s 0 through c1-1
print printBits(b)
# n = n | b inserts 1s at positions 0 through c1 -1
'''

'''
Next Number: Given a positive integer, print the next smallest and the next largest number that have the same. number of 1 bits in their binary representation
'''
class Solution:
	def nextNumbers(self, num):
		def getNext(num):
			# 1. Flip rightmost non-trailing 0. This is p
			# 2. Clear bits to the right of p 
			# Let c1 be the number of ones to the right of p
			# Let c0 be the number of zeros to the right of p
			# 3. Add in c1 - 1 (account for p)

			n = num
			c0 = c1 = 0
			while (n & 1) != 1 and n != 0:
				c0 += 1
				n = n >> 1 

			print "c0 %d" % c0

			while (n & 1) == 1:
				c1 += 1
				n = n >> 1

			print "c1 %d" % c1

			if (c0 + c1 == 31) or (c0 + c1 == 0):
				return -1

			p = c0 + c1

			print "p %d" % p

			#flip p bit
			#clear bits to left of p
			#add c1-1 bits back in to left of

			printBits(num) 
			num |= (1 << p)
			printBits(num) 
			mask = ~((1 << p) - 1)
			num &= mask
			printBits(num)

			mask = (1 << c1 - 1) - 1
			num |= mask
			
			printBits(num)
			return num

		def getPrev(num):
			# count right most 1s (c1)
			# count 0s after 
			# p = c0 + c1

			# clear bit @ p
			# clear bits to left of p
			# flip c1 + 1 bits immediately to the right of p

			n = num
			c1 = c0 = 0
			while (n & 1) != 0:
				c1 += 1
				n = n >> 1

			if n == 0:
				return -1

			while (n & 1) == 0 and n != 0:
				c0 += 1
				n = n >> 1

			p = c0 + c1
			
			printBits(num)

			num &= (~0) << (p+1)

			printBits(num)

			mask = ((1 << c1+1)-1 << (c0 - 1))

			printBits(mask)

			num |= mask
			printBits(num)
			return num

		return [getNext(num), getPrev(num)]


print Solution().nextNumbers(13948) #next = p = 7, c0 = 2, c1 = 5, expect 11011010001111 ('13967')
print Solution().nextNumbers(13967) #next = expect ('13948')
print Solution().nextNumbers(10115) #10011110000011, previous = c1 = 2, c0 = 5, p = 7, expect 10011101110000 ('10096')


