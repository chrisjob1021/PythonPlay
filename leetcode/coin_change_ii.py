class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        for coin in coins:
            for i in xrange(1, amount+1):
                if coin <= i:
                    dp[i] += dp[i - coin]

        return dp[amount]

print Solution().change(5, [1,2,5]) # 4
print Solution().change(3, [2]) # 0
print Solution().change(10, [10]) # 1
