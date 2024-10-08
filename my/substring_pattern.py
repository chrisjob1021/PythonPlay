'''
https://leetcode.com/problems/repeated-substring-pattern/?tab=Description

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

Example:
s1 = abababab
s2 = bababa

'''

class Solution(object):
	def repeatedSubstringPattern(self, string):
		solution = (string + string)[1:-1]
		return solution.find(string) != -1

print Solution().repeatedSubstringPattern("abab") # true
print Solution().repeatedSubstringPattern("aba") # false
print Solution().repeatedSubstringPattern("abcabcabcabc") # true