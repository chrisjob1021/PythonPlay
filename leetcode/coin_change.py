class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [amount+1] * amount
        for i in xrange(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] > amount else dp[amount]


print Solution().coinChange([1, 2, 5], 11) # 3
print Solution().coinChange([2], 3) # -1
print Solution().coinChange([1], 0)
