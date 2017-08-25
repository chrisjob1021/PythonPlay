class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        d1 = { }
        d2 = { }
        
        for c in [c.lower() for c in s]:
            d1[c] = d1.get(c, 0) + 1
        
        for c in [c.lower() for c in t]:
            d2[c] = d2.get(c, 0) + 1
        
        return d1 == d2

    def maxAnagram(self, words):
    	res = { } 

    	import itertools

    	for word in itertools.permutations(words, 2):
    		print word[0], word[1]
    		if self.isAnagram(word[0], word[1]):
    			res[word[0]] = res.get(word[0], 1) + 1

    	return sorted(res.values(), reverse=True)[0]

print Solution().maxAnagram(["aaaa", "AAAA", "abac", "baac", "caba", "cat"])