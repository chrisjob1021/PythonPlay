'''

https://leetcode.com/problems/longest-substring-without-repeating-characters/?tab=Description#/description

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, string):
        start = 0
        maxL = 0 

        solution = { }

        for i in xrange(len(string)):
            if string[i] in solution and start <= solution[string[i]]:
                start = solution[string[i]] + 1
            else:
                maxL = max(maxL, i - start + 1)

            solution[string[i]] = i

        return maxL


print Solution().lengthOfLongestSubstring("abcabcbb") #3
print Solution().lengthOfLongestSubstring("bbbbb") #1
print Solution().lengthOfLongestSubstring("pwwkew") #3
print Solution().lengthOfLongestSubstring("abcabcbbabcd") #4
print Solution().lengthOfLongestSubstring("abbacabcd") #4