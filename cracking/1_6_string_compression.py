#O(n + j) j == number of charsets

class Solution:
	def compressString1(self, s):
		slist = list(s)
		newstring = [ ]
		n = len(slist)

		def sub(slist, start, end):
			count = 1

			for j in xrange(start+1, end): # O(j)
				if slist[j] == slist[start]:
					count += 1
				else:
					return [count, j]

			return [count, start+1]

		i = 0
		while i < n: #O(n)
			newstring.append(slist[i]) #O(1)
			(count, i) = sub(slist, i, n) 
			newstring.append(str(count)) #O(1)

		# O(n)
		return ''.join(newstring) if len(newstring) < n else s

print Solution().compressString1("aaaaaaab")
print Solution().compressString1("abc")






