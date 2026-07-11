class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def dfs(rem: int) -> int:
            # Base cases
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            min_coins = float('inf')
            
            # Explore every coin choice
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_coins = min(min_coins, res + 1)

            # Store the computed minimum in cache
            memo[rem] = min_coins if min_coins != float('inf') else -1
            return memo[rem]

        return dfs(amount)
