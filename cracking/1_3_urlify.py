class Solution:
	def URLify(self, s, length):
		strList = list(s)

		for i in xrange(length):
			if strList[i] == " ":
				strList[i] = "%20"

		return ''.join(strList[:length])

print Solution().URLify("Mr John Smith    ", 13)