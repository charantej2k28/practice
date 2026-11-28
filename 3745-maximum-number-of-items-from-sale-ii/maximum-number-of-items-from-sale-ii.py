from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # Count frequency of each factor (1 <= factor <= n)
        freq = [0] * (n + 1)
        min_price = float('inf')
        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p
                
        # Calculate how many other items have a factor divisible by f
        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] == 0:
                continue
            total = 0
            for mult in range(f, n + 1, f):
                total += freq[mult]
            multiples[f] = total - 1
            
        # Sort items by price ascending to greedily take 2-item bundles
        items.sort(key=lambda x: x[1])
        
        # Baseline: spend entire budget on the single cheapest item (1 copy each)
        ans = budget // min_price
        
        rem_budget = budget
        cur_items = 0
        
        for f, p in items:
            # A 2-item bundle at price p is never better than two 1-item buys at min_price
            if p >= 2 * min_price:
                break
                
            slots = multiples[f]
            if slots <= 0:
                continue
                
            # Maximum 2-item bundles we can buy for this item
            take = min(slots, rem_budget // p)
            if take == 0:
                break
                
            # Check stopping 1 bundle short in case the leftover budget fits more min_price items
            if take >= 1:
                temp_rem = rem_budget - (take - 1) * p
                temp_items = cur_items + (take - 1) * 2
                ans = max(ans, temp_items + temp_rem // min_price)
                
            rem_budget -= take * p
            cur_items += take * 2
            
            # Evaluate total items after taking all possible bundles of this item
            ans = max(ans, cur_items + rem_budget // min_price)
            
        return ans