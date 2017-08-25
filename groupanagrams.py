class Solution(object):
	def groupAnagrams(self, strs):
		if len(strs) == 0:
			return []

		d = { }

		for word in strs:
			s = ''.join(sorted([c.lower() for c in word]))
			d[s] = d.get(s, []) + [word]

		return d.values()

print max(map(len,Solution().groupAnagrams(["aaaa", "AAAA", "abac", "baac", "caba", "cat"])))
print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])