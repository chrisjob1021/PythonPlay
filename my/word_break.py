'''
https://leetcode.com/problems/word-break/?tab=Description

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

The idea is the following:

d is an array that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.

'''

class Solution(object):
	def wordBreak(self, s, words):
		n = len(s)
		solution = [False] * n

		for i in xrange(n):
			for w in words:
				if s[i-len(w)+1:i+1] == w and (solution[len(w)-1] or (i-len(w)) == -1):
					solution[i] = True

		print solution
		return solution[-1]

			
s = "leetcode"
words = ["code", "leet"]
print Solution().wordBreak(s, words)