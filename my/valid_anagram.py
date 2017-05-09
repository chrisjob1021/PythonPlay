'''

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

'''
class Solution(object):
	def validAnagram(self, s, t):
		result1 = { }
		result2 = { }
		for char in s:
			result1[char] = result1.get(char, 0) + 1

		for char in t:
			result2[char] = result2.get(char, 0) + 1

		return result1 == result2

	def validAnagram2(self, s, t):
		result1 = [0]*26
		result2 = [0]*26

		for char in s:
			result1[ord(char)-ord('a')] += 1
		for char in t:
			result2[ord(char)-ord('a')] += 1	

		return result1 == result2




s = "anagram"
t = "nagaram"
print Solution().validAnagram(s, t)


s = "rat"
t = "car"
print Solution().validAnagram(s, t)


s = "anagram"
t = "nagaram"
print Solution().validAnagram2(s, t)

s = "rat"
t = "car"
print Solution().validAnagram2(s, t)