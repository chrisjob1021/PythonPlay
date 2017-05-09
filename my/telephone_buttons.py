'''

https://leetcode.com/problems/letter-combinations-of-a-phone-number/?tab=Solutions

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''

class Solution(object):
	def letterCombinations(self, digits):
		if digits == '': return [ ]

		keymap = {
		    '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
		}

		'''
		http://stackoverflow.com/questions/9108855/how-does-reduce-function-work

		def myreduce(func, iterable, start=None):
	    it = iter(iterable)
	    if start is None:
	        try:
	            start = next(it)
	        except StopIteration:
	            raise TypeError('reduce() of empty sequence with no initial value')
	    accum_value = start
	    for x in iterable:
	        accum_value = func(accum_value, x)
	    return accum_value
		'''

		# start with last argument aka initializer = a list with empty string

		# The "reduce" function will transform a given list into a single value by applying a given function continuously to all the elements. 
		# It basically keeps operating on pairs of elements until there are no more elements left.

		# start with [''] as 'x'
		# add keymap['2']
		# add keymap['3']
		# repeat until there are no more chars

		return reduce(lambda acc, digit: [x + y for x in acc for y in keymap[digit]], digits, [''])

print Solution().letterCombinations('23')