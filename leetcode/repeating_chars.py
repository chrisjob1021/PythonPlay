'''

https://leetcode.com/problems/longest-substring-without-repeating-characters/?tab=Description

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

#O(n)
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		# set starting position and maxlength to 0
		start = maxLength = 0
		# create dict to represent last seen character position of letter
		used = { } 

		for i in range(len(s)):
			# if character in dict and start is less than last seen character position of letter
			# reset start to last seen character position
			if s[i] in used and start <= used[s[i]]:
				# set start after this character (+ 1)
				start = used[s[i]] + 1
			else:
				# set max length to the larger of two values
				# previously set maxlength
				# or
				# i (representing 0 start of length) - start position of not repeating characters + 1 (to represent length and not 0 index)
				maxLength = max(maxLength, i - start +1)

			# set last seen position of character
			used[s[i]] = i

		return maxLength

print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("bbbbb")
print Solution().lengthOfLongestSubstring("pwwkew")
