'''
https://leetcode.com/problems/longest-palindromic-subsequence/?tab=Description

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

'''

class Solution(object):
	def longestPalSub(self, s):
		d = { }

		def palsub(s):
			if s not in d:
				maxL = 0 

				for c in set(s): #IMPORTANT
					i = s.find(c)
					j = s.rfind(c)

					maxL = max(maxL, 1 if i==j else 2+palsub(s[i+1:j]))

				d[s] = maxL

			return d[s]

		return palsub(s)



print Solution().longestPalSub("bbbab") # 4
print Solution().longestPalSub("cbbd") # 2
print Solution().longestPalSub("AABCDEBAZ") # 5