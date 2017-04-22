class Solution:
	def printNum(self, num):
		print '{:3}'.format(num), 
		# get 7 bits set
		# and it with num to get true binary representation for negative numbers
		print bin(num)
		print bin((1 << 7) - 1 & num) 

	def getBit(self, num, i):
		self.printNum(num)
		# shift 1 by i bits
		# by performing AND with num, you are left with 1 at only i location
		# if new value is 1, then we know the bit is set at i
		return ((num & (1 << i)) != 0)
	def setBit(self, num, i):
		self.printNum(num)
		# shift 1 by i bits
		# by performing OR with num, the result will that it will only set a bit at i location
		newnum = num | (1 << i)
		self.printNum(newnum)

	def clearBit(self, num, i):
		self.printNum(num)
		# create inverse of number
		# AND it
		mask = ~(1 << i)
		newnum = num & mask

		self.printNum(newnum)

	def clearMSBThruI(self, num, i):
		self.printNum(num)
		mask = (1 << i) - 1
		self.printNum(mask)

		newnum = num & mask
		self.printNum(newnum)

	def clearIThru0(self, num, i):
		self.printNum(num)
		mask = (-1 << (i+1))
		self.printNum(mask)

		newnum = num & mask
		self.printNum(newnum)

	def updateBit(self, num, i, bitIs1):
		self.printNum(num)
		value = 1 if bitIs1 else 0

		#clear the bit at position i by using mask that looks like 11101111
		mask = ~(1 << i) # e: 11101111
		self.printNum(mask)

		#then shift the intended value, v, left by i bits
		#this will create a number with bit i equal to v and all other bits equal to 0

		#finally we OR these two numbers, updating the ith bit if v ==1 or leaving as 0 otherwise
		newnum = (num & mask) | (value << i)
		self.printNum(newnum)




#print Solution().getBit(2,0)
#print Solution().setBit(2,0)
#Solution().clearBit(3,0)
#Solution().clearIThru0(100, 2)
Solution().updateBit(100, 2, False)