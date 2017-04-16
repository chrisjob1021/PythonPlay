# Remember to convert to lower

# keep running bits
# toggle 

class Solution:
	def isPalindromePerm(self, string):
		def toggle(bits, i):
			if i < 0:
				return bits

			mask = 1 << i
			if (bits & mask) == 0:
				#print 'mask: %s, bits after bits AND mask: %s' % ('{0:b}'.format(mask), '{0:b}'.format(bits & mask))
				#print "so we flip a bit on"
				bits += mask
			else:
				bits &= ~mask
				#print 'mask: %s, bits after bits += NOT mask: %s' % ('{0:b}'.format(mask), '{0:b}'.format(bits & mask))

			return bits

		bits = 0 
		for char in string.lower():
			index = ord(char) - ord('a')
			#print 'current `bits` variable: %s' % ('{0:b}'.format(bits))
			#print 'index: %d, index\'s bits: %s' % (index, '{0:b}'.format(index))
			bits = toggle(bits, index)
			print char, '{0:b}'.format(bits)

		return bits == 0 or (bits & (bits-1)) == 0

print Solution().isPalindromePerm("Tact Coa")
print Solution().isPalindromePerm("abc")
print Solution().isPalindromePerm("aab")
print Solution().isPalindromePerm("back cajaputs stupa jack cab")


