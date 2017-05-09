'''
https://leetcode.com/problems/count-primes/?tab=Solutions

Description:

Count the number of prime numbers less than a non-negative number, n.

'''

class Solution(object):
	def countPrimes(self, n):
		if n < 3:
			return 0

		primes = [True] * n

		primes[0] = False
		primes[1] = False

		for i in xrange(2,int(n**0.5+1)):
			primes[i*i:n:i] = [False] * len(primes[i*i:n:i])

		return sum(primes)

print Solution().countPrimes(37) # 11