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

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if digits == '': return ['']
        key_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        return reduce(lambda acc, digit: [ x + y for x in acc for y in key_map[digit]], digits, [''])

print Solution().letterCombinations("23")
