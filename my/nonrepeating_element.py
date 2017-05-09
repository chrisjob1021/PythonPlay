'''
http://stackoverflow.com/questions/29333689/how-to-find-the-only-number-in-an-array-that-doesnt-occur-twice

You can define an integer "result" initialized to 0, and then you do some bitwise operations by applying a XOR logic to all elements in your array.

At the end, "result" will be equal to the only element that appears only one time.

result = 0
for i in array:
  result ^= i
return result
http://en.wikipedia.org/wiki/Bitwise_operation#XOR

For instance, if your array contains the elements [3, 4, 5, 3, 4], the algorithm will return

3 ^ 4 ^ 5 ^ 3 ^ 4

But the XOR operator ^ is associative and commutative, so the result will be also equal to:

(3 ^ 3) ^ (4 ^ 4) ^ 5

Since i ^ i = 0 for any integer i, and i ^ 0 = i, you have

(3 ^ 3) ^ (4 ^ 4) ^ 5 = 0 ^ 0 ^ 5 = 5

'''

array = [ 1, 2, 2, 2, 3, 3, 4, 4, 2 ]

result = 0
for element in array:
	print element
	result ^= element
	print result
print result