# ascii vs. unicode 
# assume ascii

class Solution:
	# Time: O(n)
	# Space: O(1)
	def isUnique1(self, s):
		if len(s) > 128:
			return False

		res = [False] * 128

		for c in s:
			val = ord(c)
			if res[val]:
				return False
			else:
				res[val] = True

		return True

	# assume a-z and use bit vector
	# Time: O(n)
	# Space: O(1), but less
	def isUnique2(self, s):
		if len(s) > 26:
			return False

		checker = 0

		for c in s:
			val = ord(c) - ord('a')

			if (checker & (1 << val) > 0):
				return False
			else:
				checker += 1 << val

		return True

	# Time: O(n*n)
	# Space: O(1) with no addt'l data structures
	def isUnique3(self, s):
		n = len(s)
		if n > 26:
			return False

		for i in xrange(n):
			for j in xrange(i+1,n):
				if s[i] == s[j]:
					return False
		return True


print Solution().isUnique3("abc")
print Solution().isUnique3("cdc")

