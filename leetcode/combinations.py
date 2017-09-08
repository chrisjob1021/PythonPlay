class Solution(object):
	def combinations(self, n, k):
		if k == 0:
			return [[]]

		return [[i] + path for i in xrange(1,n+1) for path in self.combinations(i-1, k-1)]

print Solution().combinations(4,2)