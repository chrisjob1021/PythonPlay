'''

https://leetcode.com/problems/first-unique-character-in-a-string/?tab=Description

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

'''

class Solution(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c in s if s.count(c)==1] or [-1])

print Solution().firstUniqChar("leetcode")
print Solution().firstUniqChar("loveleetcode")
print Solution().firstUniqChar("hihihello")