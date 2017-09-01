class Solution:
    def coinChange(self, coins, amount):
        if amount < 1:
            return 0

        return self.helper(coins, amount, {})

    def helper(self, coins, amount, d):
        if amount == 0:
            return 0

        if amount in d:
            return d[amount]

        n = amount + 1

        for coin in coins:
            curr = 0
            if amount >= coin:
                nextrun = self.helper(coins, amount-coin, d)
                if nextrun >= 0:
                    curr = 1 + nextrun

            if curr > 0:
                n = min(n, curr)

        if n == amount + 1:
            final = -1
        else:
            final = n

        d[amount] = final
        return final

print Solution().coinChange([1, 5], 6)

'''
https://discuss.leetcode.com/topic/35720/easy-to-understand-recursive-dp-solution-using-java-with-explanations

public class Solution {
    Map<Integer,Integer> amountDict = new HashMap<Integer,Integer>();
    public int coinChange(int[] coins, int amount) {
        if(amount==0)
            return 0;
        if(amountDict.containsKey(amount))
            return amountDict.get(amount);
        int n = amount+1;
        for(int coin : coins) {
            int curr = 0;
            if (amount >= coin) {
                int next = coinChange(coins, amount-coin);
                if(next >= 0)
                    curr = 1+next;
            }
            if(curr > 0)
                n = Math.min(n,curr);
        }
        int finalCount = (n==amount+1) ? -1 : n;
        amountDict.put(amount,finalCount);
        return finalCount;
    }
}
'''