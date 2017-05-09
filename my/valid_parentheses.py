'''
https://leetcode.com/problems/valid-parentheses/?tab=Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution(object):
	def validParentheses(self, string):
		valid = {
			")": "(",
			"}": "{",
			"]": "["
		}

		stack = [ ]

		for char in string:
			if char in valid.values():
				stack.append(char)
			elif char in valid.keys():
				if stack == [ ] or valid[char] != stack.pop():
					return False
			else:
				return False

		return stack == [ ]	


print Solution().validParentheses("()")
print Solution().validParentheses("()[]{}")
print Solution().validParentheses("(]")
print Solution().validParentheses("([)]")
print Solution().validParentheses("()[]{}(")
