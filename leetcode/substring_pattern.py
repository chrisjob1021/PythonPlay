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

Basic idea:

First char of input string is first char of repeated substring
Last char of input string is last char of repeated substring
Let S1 = S + S (where S in input string)
Remove 1 and last char of S1. Let this be S2
If S exists in S2 then return true else false
Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]

Example:
s1 = abababab
s2 = bababa

'''

class Solution(object):
	def repeatedSubstringPattern(self, str):
	        """
	        :type str: str
	        :rtype: bool
	        """
	        if not str:
	            return False
	            
	        ss = (str + str)[1:-1]
	        return ss.find(str) != -1

print Solution().repeatedSubstringPattern("abab")