# Best case: O(s1 + s2)
# Space could be optimized from O(n) to O(1) using bitwise operators

class Solution:
	def permOfOther1(self, s1, s2):
		if len(s1) != len(s2):
			return False

		d1 = {}
		d2 = {}

		for char in s1:
			d1[char] = d1.get(char, 0) + 1

		for char in s2:
			d2[char] = d2.get(char, 0) + 1 

		return d1 == d2

	def permOfOther2(self, s1, s2):
		if len(s1) != len(s2):
			return False

		result = 0 

		for char in s1:
			result ^= ord(char)

		for char in s2:
			result ^= ord(char)

		return result == 0

	# third possible solution: create a list, increment value by 1 for s1, decrement value by 1 for s2
	# if less than 0, exit early

print Solution().permOfOther1("aba", "baa")
print Solution().permOfOther1("abc", "cde")

print Solution().permOfOther1("aba", "baa")
print Solution().permOfOther2("abc", "cde")