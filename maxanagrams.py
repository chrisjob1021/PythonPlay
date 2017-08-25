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

#    def maxAnagram(self, words):
#    	res = { } 
#
#    	import itertools
#
#    	for word in itertools.permutations(words, 2):
#    		print word[0], word[1]
#    		if self.isAnagram(word[0], word[1]):
#    			res[word[0]] = res.get(word[0], 1) + 1
#
#    	return sorted(res.values(), reverse=True)[0]
    def maxAnagram(self, words):
        d = { }

        for word in words:
            s = ''.join(sorted([c.lower() for c in word]))

            d[s] = d.get(s, 0) + 1

        print [k for k in d.keys() if d.get(k) > 1]
        return max(d.values())

print Solution().maxAnagram(["aaaa", "AAAA", "abac", "baac", "caba", "cat"])
print Solution().maxAnagram(["eat", "tea", "tan", "ate", "nat", "bat"])