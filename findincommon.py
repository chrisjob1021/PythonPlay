class Solution:
	def findInCommon(self, l1, l2):
		def linearSearch(l, item, start):
			for i in xrange(start, len(l)):
				if item == l[i]:
					return [True, i+1]
				elif l[i] > item:
					return [None, i]
			
			return [None, start]

		sol = [ ]
		start = 0
		res = None
		for elem in l1:
			print (res, start)
			(res, start) = linearSearch(l2, elem, start)
			if res == True:
				sol.append(elem)


		return sol

print Solution().findInCommon(sorted([8, 10, 1, 6, 3]), sorted([5, 3, 10, 4, 7]))



