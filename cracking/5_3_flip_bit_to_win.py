'''
You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of 1s you could create.
'''

class Solution:
	# Time: O(b) b = length of sequence
	# Space: O(b)
	def longestSequence(self, n):
		'''
		Return a list of the sizes of the sequences.
		The sequence starts off with the number of 0s and then alternates with the counts of each value.
		'''
		def getAlternatingSequences(n):
			sequences = [ ]

			searchingFor = 0
			counter = 0

			print '{0:b}'.format(n)
			length = len('{0:b}'.format(n))

			for i in xrange(length):
				if ((n & 1) != searchingFor):
					sequences.append(counter)
					searchingFor = n & 1
					counter = 0
				counter += 1
				n = n >> 1
			sequences.append(counter)

			print sequences
			return sequences

		def findLongestSequence(sequences):
			maxSeq = 1

			# step by 2 because we alternate 0s and 1s in our sequences list
			for i in xrange(0, len(sequences), 2):
				zerosSeq = sequences[i]
				onesSeqLeft = sequences[i-1] if i - 1 >= 0 else 0
				onesSeqRight = sequences[i+1] if i + 1 < len(sequences) else 0 

				print zerosSeq, onesSeqLeft, onesSeqRight

				if zerosSeq == 1: # we can merge because we can flip 1 bit of this sequence
					thisSeq = onesSeqLeft + 1 + onesSeqRight
				elif zerosSeq > 1: # we can flip a bit on either side
					thisSeq = 1 + max(onesSeqLeft, onesSeqRight)
				elif zerosSeq == 0: #take the max of left or right side
					thisSeq = max(onesSeqLeft, onesSeqRight)

				maxSeq = max(thisSeq, maxSeq)

			return maxSeq

		sequences = getAlternatingSequences(n)
		return findLongestSequence(sequences)


print Solution().longestSequence(1775)