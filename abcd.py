class Solution:
	def positive(self, n):
		m = { }
		for c in xrange(1,n):
			for d in xrange(1,n):
				result = pow(c, 3) + pow(d, 3)
				m[result] = [c, d]
		for v in m.itervalues():
			print v*2

print Solution().positive(20)

