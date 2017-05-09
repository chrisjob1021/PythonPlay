'''
https://leetcode.com/problems/longest-palindromic-subsequence/?tab=Description

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        d = {}
        def f(s):
        	# if string not in dictionary
            if s not in d:
                maxL = 0    
                print set(s)
                for c in set(s):
                	# set i to lowest index of char
                	# set j to highest index of char
                    i, j = s.find(c), s.rfind(c)
                    # take max of 0 
                    # or, 1 if there's only one occurrence of character
                    # or 2 + result of recursive function call with string slice of i+1 to j 
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                # add palindromic subsequence to dictionary
                d[s] = maxL
         	# return last instance of function call after recursion
            return d[s]
        # called f() separately so d would not be overwritten by recursive function call
        return f(s)

print Solution().longestPalindromeSubseq("AABCDEBAZ")