'''
https://leetcode.com/problems/reverse-words-in-a-string-ii/?tab=Description

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        slist = s.split()
        return ' '.join(slist[::-1])

s = "the sky is blue"
print Solution().reverseWords(s)