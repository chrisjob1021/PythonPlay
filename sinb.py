class Solution:
	def findS(self, s, b):
		# O(b * s)
		sD = { }
		# O(s)
		for c in s:
			sD[c] = sD.get(c, 0) + 1

		slen = len(s)
		blen = len(b)
		sol = []
		# O(b)
		for i in xrange(blen):
			bD = { }
			# O(s)
			for c in b[i:i+slen]:
				bD[c] = bD.get(c, 0) + 1
			if sD == bD:
				sol.append((i, i+slen))

		return [len(sol), sol]

print Solution().findS("abbc", "cbabadcbbabbcbabaabccbabc")