'''

https://leetcode.com/problems/valid-parentheses/?tab=Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, string):
        print string

        stack = [ ]
        valid_dict = { "}": "{", "]": "[", ")": "(" }

        for char in string:
            if char in valid_dict.values():
                stack.append(char)
            elif char in valid_dict.keys():
                if stack == [ ] or valid_dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == [ ]

for string in [ "()", "()[]{}(", "(]", "([)]" ]:
    print Solution().isValid(string)