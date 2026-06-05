class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        max=float("inf")
        for i in range(1,amount+1):
            dp[i]=max
            for coin in coins:
                if coin <=i and dp[i-coin]!=max:
                    dp[i]=min(dp[i],1+dp[i-coin])
        return dp[amount] if dp[amount]!=max else -1