# only afforded 1 call
# need same number of characters
# same characters
# characters can't be in same order

# O(n)

class Solution:
	def isSubstring(self, s1, s2):
		n = len(s1)

		if s1 == s2 or n != len(s2):
			return False 

		s1d = { }
		s2d = { }

		for i in xrange(n):
			s1d[s1[i]] = i

		for i in xrange(n): 
			s2d[s2[i]] = i

		if s1d.keys() != s2d.keys():
			return False

		return True
	def isSubstring2(self, s1, s2):
		def substring(string, target):
			if len(string) > len(target):
				return False

			if string == target:
				return True

			return substring(string, target[:len(target)-1]) or substring(string, target[1:])

		n = len(s1)

		if s1 == s2 or n != len(s2):
			return False 

		ss = s1 + s2
		return substring(s1, ss) #O(n)
		#return ss.find(s1) != -1 # worst case, O(ss * s1)


		


print Solution().isSubstring2("waterbottle", "erbottlewat")
print Solution().isSubstring2("waterbottle", "waterbottle")
