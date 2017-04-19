class Solution:
	def rotate(self, matrix):
		def printMatrix(matrix):
			for row in matrix:
				for i in xrange(len(row)):
					print '{:2}'.format(row[i]),
				print
			print

		n = len(matrix)
		if n == 0 or n != len(matrix[0]):
			return False

		printMatrix(matrix)

		for layer in xrange((n/2)):
			first = layer
			last = n - 1 - layer
			#print "first %d, last %d" % (first, last)

			for i in xrange(first, last):
				offset = i - first
				#print "i %d, offset %d" % (i, offset)

				# save top
				top = matrix[first][i]

				# first 	0	  0
				# last 		3     3
				# i 		0     1
				# offset 	3     1

				# top	top 	X 		right 
				#  X 	X 		X 		right
				# left 	X 		X 		X 
				# left  X		bottom	bottom

				# top = left
				matrix[first][i] = matrix[last-offset][first]

				# left = bottom
				matrix[last-offset][first] = matrix[last][last-offset]

				# bottom = right
				matrix[last][last-offset] = matrix[i][last]

				# right = top
				matrix[i][last] = top

		printMatrix(matrix)

matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

Solution().rotate(matrix)