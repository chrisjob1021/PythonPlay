'''

'''

class Solution:
	def oneAway(self, first, second):
		if abs(len(first) - len(second)) > 1:
			return False

		# i2 = longer
		# i1 = shorter
		i1 = i2 = 0

		string1 = first if len(first) < len(second) else second
		string2 = second if len(first) < len(second) else first

		foundDiff = False
		while (i2 < len(string2)) and (i1 < len(string1)):
			if string2[i2] != string1[i1]:
				if foundDiff:
					return False
				
				foundDiff = True
				if len(string1) == len(string2):
					i1 += 1
			else:
				i1 += 1

			i2 += 1

		return True

print Solution().oneAway("pale", "ple") #true
print Solution().oneAway("pales", "pale") # true
print Solution().oneAway("pale", "bale") # true
print Solution().oneAway("pale", "bake") # false
print Solution().oneAway("plle", "ple") # true
print Solution().oneAway("plae", "plla") #false 
print Solution().oneAway("plae", "plaedd") # false