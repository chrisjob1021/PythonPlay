class Solution:
	def perms(self, s):
		n = len(s)

		res = [ ]

		def sub(start, path):
			res.append(path)
			for i in xrange(start,n):
				path.append(s[i])
				sub(i+1, path)

		sub(0, [])
		print res



print Solution().perms("ab")