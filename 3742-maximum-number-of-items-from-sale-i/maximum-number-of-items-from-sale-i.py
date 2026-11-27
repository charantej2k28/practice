from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MAX_F = 1500
        freq = [0] * (MAX_F + 1)
        for f, _ in items:
            freq[f] += 1
            
        # Precompute total items whose factor is a multiple of f (including self)
        multiples_count = [0] * (MAX_F + 1)
        for f in range(1, MAX_F + 1):
            if freq[f] > 0:
                for m in range(f, MAX_F + 1, f):
                    multiples_count[f] += freq[m]
                    
        # dp[c] = max items obtained using exact cost c for "first copies"
        dp = [-1] * (budget + 1)
        dp[0] = 0
        min_price = float('inf')
        
        for f, p in items:
            if p < min_price:
                min_price = p
            if p > budget:
                continue
                
            # 1 purchased copy + free copies of all j != i where f divides factor_j
            first_copy_val = multiples_count[f] 
            
            # 0/1 Knapsack transition (iterate backwards)
            for c in range(budget, p - 1, -1):
                if dp[c - p] != -1:
                    if dp[c - p] + first_copy_val > dp[c]:
                        dp[c] = dp[c - p] + first_copy_val
                        
        # Fill any remaining budget with copies of the cheapest item (value 1 per copy)
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra_copies = (budget - c) // min_price
                ans = max(ans, dp[c] + extra_copies)
                
        return ans