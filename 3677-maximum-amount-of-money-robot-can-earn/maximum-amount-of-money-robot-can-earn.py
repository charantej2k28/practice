class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m, n = len(coins), len(coins[0])
        neg_inf = -float('inf')
        
        dp = [[[neg_inf] * 3 for _ in range(n)] for _ in range(m)]
        
        val = coins[0][0]
        dp[0][0][0] = val
        if val < 0:
            dp[0][0][1] = 0
            dp[0][0][2] = 0
        else:
            dp[0][0][1] = val
            dp[0][0][2] = val
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = coins[i][j]
                for k in range(3):
                    best_prev = neg_inf
                    if i > 0:
                        best_prev = max(best_prev, dp[i - 1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j - 1][k])
                    
                    if best_prev != neg_inf:
                        dp[i][j][k] = max(dp[i][j][k], best_prev + val)
                    
                    if k > 0:
                        best_prev_k1 = neg_inf
                        if i > 0:
                            best_prev_k1 = max(best_prev_k1, dp[i - 1][j][k - 1])
                        if j > 0:
                            best_prev_k1 = max(best_prev_k1, dp[i][j - 1][k - 1])
                        
                        if best_prev_k1 != neg_inf:
                            dp[i][j][k] = max(dp[i][j][k], best_prev_k1 + max(0, val))

        return max(dp[m - 1][n - 1])