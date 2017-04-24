'''
You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of 1s you could create.
'''

class Solution:
	def longestSequence(self, num):
		def generateSequences(num):
			sequences = [ ]

			count = 0
			target = 0

			# get binary length of integer
			length = len('{0:b}'.format(num))

			for i in xrange(length):
				if (num & 1) != target:
					sequences.append(count)
					target = num & 1
					count = 0

				count += 1
				num = num >> 1

			sequences.append(count)	

			print sequences
			return sequences


		def countLongestSequence(sequences):
			maxSeq = 1
			currSeq = 0

			# count by 2 because we alternate between 0s and 1s
			for i in xrange(0, len(sequences), 2):
				zeros = sequences[i]
				left = sequences[i - 1] if i - 1 > 0 else 0
				right = sequences[i + 1] if i + 1 < len(sequences) else 0

				if zeros == 1:
					currSeq = 1 + left + right
				elif zeros > 1:
					currSeq = 1 + max(left, right)
				elif zeros == 0:
					currSeq = max(left, right)

				maxSeq = max(maxSeq, currSeq)

			return maxSeq

		print '{0:b}'.format(num)

		sequences = generateSequences(num)
		return countLongestSequence(sequences)

print Solution().longestSequence(1775) # 8