'''
https://leetcode.com/problems/count-primes/?tab=Solutions

Description:

Count the number of prime numbers less than a non-negative number, n.

'''

class Solution:
	def countPrimes(self, n):
		# no more than one prime number less than 3 (2)
		# so 2 would have 0 prime numbers less than it
	    if n < 3:
	        return 0
	    # create a list containing true times n
	    primes = [True] * n

	    # kudos to dimitar
	    # list index is representing actual prime numbers
	    # 0 and 1 are not primes
	    primes[0] = primes[1] = False

	    '''
	    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

	    Example--

	    To find all the prime numbers less than or equal to 30, proceed as follows.

		First generate a list of integers from 2 to 30:

		The first number in the list is 2; cross out every 2nd number in the list after 2 by counting up from 2 in increments of 2 (these will be all the multiples of 2 in the list):

		The next number in the list after 2 is 3; cross out every 3rd number in the list after 3 by counting up from 3 in increments of 3 (these will be all the multiples of 3 in the list):

		The next number not yet crossed out in the list after 3 is 5; cross out every 5th number in the list after 5 by counting up from 5 in increments of 5 (i.e. all the multiples of 5):

		The next number not yet crossed out in the list after 5 is 7; the next step would be to cross out every 7th number in the list after 7, but they are all already crossed out at this point, as these numbers (14, 21, 28) are also multiples of smaller primes because 7 x 7 is greater than 30. The numbers not crossed out at this point in the list are all the prime numbers below 30:

		When testing each prime, the optimal trial division algorithm uses all prime numbers not exceeding its square root, whereas the sieve of Eratosthenes produces each composite from its prime factors only, and gets the primes "for free", between the composites. The widely known 1975 functional sieve code by David Turner[12] is often presented as an example of the sieve of Eratosthenes[6] but is actually a sub-optimal trial division algorithm.[2]

	    '''

	    # for i in range from 2 to n ** 0.5 (exponential (power) calculation) + 1
	    for i in range(2, int(n ** 0.5) + 1):
	        # if list has True value @ i
	        if primes[i]:
	            # set false for non-primes in list:
		            # starting at i squared
		            # to n (number of possible results)
		            # incrementing by i

	            '''
					W whglamrock 
					Reputation:  32
					if you try:

					primes = [1,2,3,4,5,6,7,8,9,10]

					primes[3:10:2] = [0]*len(primes[3:10:2])

					print primes

					you will see what's going on.
	            '''
	            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

	    print {x: primes[x] for x in range(n)}
	    # return number of True's
	    return sum(primes)

print Solution().countPrimes(37)