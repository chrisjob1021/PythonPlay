'''even number of characters 
or odd number of characters, accounting for the middle number of characters
if we flip a bit on when a character is found and then turn it off when it's seen again, we will encounter a case where the bits will = 0 or there will only be one bit set
'''



class Solution:
	def isPalindromePermutation(self, s):
		def toggle(bits, index):
			if index < 0:
				return bits

			mask = 1 << index
			if (bits & mask) == 0:
				# flip bit on
				bits += mask
			else:
				# turn bit off
				bits &= ~mask

			return bits

		bits = 0
		for c in s.lower():
			index = ord(c) - ord('a')
			bits = toggle(bits, index)

		return bits == 0 or (bits & (bits-1)) == 0

print Solution().isPalindromePermutation("Tact Coa")
print Solution().isPalindromePermutation("abc")
print Solution().isPalindromePermutation("aab")
print Solution().isPalindromePermutation("back cajaputs stupa jack cab")
