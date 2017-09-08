class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(ans, [], k, 1, n)
        return ans
        
    def dfs(self, ans, path, k, start, n):
        if len(path) == k and n == 0:
            ans.append(path)
            return

        for i in xrange(start,10):
            if len(path) + 1 > k or i > n:
                break
            self.dfs(ans, path + [i], k, i+1, n-i)

print Solution().combinationSum3(3, 7)