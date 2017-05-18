class Solution:
	def nextNumbers(self, num):
		def printBinary(num):
			print '{0:15b}'.format((1 << 15) - 1 & num)

		def getNext(num):
			# count sequence of 0s to start
			# count sequence of 1s after 0s
			# flip bit after sequence of 1s
			# flip bits to start sequences, less 1 of the 1s

			c0 = c1 = 0
			n = num
			while (n & 1) == 0:
				c0 += 1
				n = n >> 1

			while (n & 1) == 1:
				c1 += 1
				n = n >> 1

			p = c0 + c1

			printBinary(num)

			# flip bit at p
			mask = 1 << p
			num = num | mask

			#printBinary(num)

			# clear everything after p
			mask = ~0 << p
			num = num & mask
			#printBinary(num)

			# add in c1-1
			mask = (1 << c1-1)-1
			num = num | mask
			printBinary(num)

			return num

		def getPrev(num):
			printBinary(num)

			c0 = c1 = 0
			n = num
			while (n & 1) == 1:
				c1 += 1
				n = n >> 1

			while (n & 1) == 0:
				c0 += 1
				n = n >> 1

			p = c0 + c1
			
			# clear everything to left of p
			mask = ~0 << p
			num = num & mask
			#printBinary(num)

			# flip bit at p
			mask = 1 << p
			num = num ^ mask
			#printBinary(num)

			mask = (1 << c1+1)-1 << c0-1
			num = num | mask
			printBinary(num)			

			return num

		return [getNext(num), getPrev(num)]

print Solution().nextNumbers(13948) #next = p = 7, c0 = 2, c1 = 5, expect 11011010001111 ('13967')
print Solution().nextNumbers(13967) #next = expect ('13948')
print Solution().nextNumbers(10115) #10011110000011, previous = c1 = 2, c0 = 5, p = 7, expect 10011101110000 ('10096')