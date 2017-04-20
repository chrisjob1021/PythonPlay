# Time: O(nm)
# Space: O(1)

class Solution:
	def setZeros(self, matrix):
		def printMatrix(matrix):
			for row in matrix:
				for element in row:
					print '{:2}'.format(element),
				print
			print


		def zeroRow(row):
			for i in xrange(len(matrix[row])):
				matrix[row][i] = 0

		def zeroColumn(column):
			for i in xrange(len(matrix)):
				matrix[i][column] = 0 

		printMatrix(matrix)

		firstRow = firstColumn = False

		for i in xrange(len(matrix[0])):
			if matrix[0][i] == 0:
				firstColumn = True

		for i in xrange(len(matrix)):
			if matrix[i][0] == 0: 
				firstRow = True

		for i in xrange(1, len(matrix)):
			for j in xrange(1, len(matrix[0])):
				if matrix[i][j] == 0:
					matrix[i][0] = 0
					matrix[0][j] = 0

		for i in xrange(len(matrix)):
			if matrix[i][0] == 0:
				zeroRow(i)

		for i in xrange(len(matrix[0])):
			if matrix[0][i] == 0:
				zeroColumn(i)

		if firstRow:
			zeroRow(0)

		if firstColumn:
			zeroColumn(0)

		printMatrix(matrix)


matrix = [
	[ 1, 2, 3, 4 ],
	[ 4, 5, 6, 7 ],
	[ 8, 9, 0, 1 ]
]

Solution().setZeros(matrix)
