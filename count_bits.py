'''
return an integer representing the total number of bits set in an object
'''

def countBits(x):
	print "{0:b}".format(x)

	count = 0
	while x > 0:
		if x&1 == 1:
			count += 1
		x = x>>1

	return count

print countBits(9)
print countBits(200)
print countBits(0)
print countBits(1)