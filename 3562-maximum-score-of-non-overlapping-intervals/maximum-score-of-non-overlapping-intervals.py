
import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Store intervals with their original 0-based index: (l, r, weight, original_idx)
        n = len(intervals)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))
        
        # Sort intervals primarily by right endpoint 'r'
        arr.sort(key=lambda x: x[1])
        
        # rights holds the right endpoints for binary search
        rights = [x[1] for x in arr]
        
        # dp[k][i] stores the best choice of at most k intervals from arr[0...i]
        # Each entry is a tuple: (score, indices_tuple)
        # We need to maximize score, and among equal scores, minimize indices_tuple lexicographically.
        dp = [[(0, ())] * n for _ in range(5)]
        
        for i in range(n):
            l, r, w, idx = arr[i]
            
            # Find the latest interval ending strictly before l: r_prev < l
            prev_idx = bisect.bisect_left(rights, l) - 1
            
            for k in range(1, 5):
                # Option 1: Do not include arr[i] in the k-interval selection
                best_without = dp[k][i - 1] if i > 0 else (0, ())
                
                # Option 2: Include arr[i] as the k-th interval
                if k == 1:
                    score_with = w
                    indices_with = (idx,)
                else:
                    if prev_idx >= 0 and dp[k - 1][prev_idx][0] > 0:
                        prev_score, prev_indices = dp[k - 1][prev_idx]
                        score_with = prev_score + w
                        # Combine and sort indices to maintain lexicographical order
                        indices_with = tuple(sorted(prev_indices + (idx,)))
                    else:
                        score_with = 0
                        indices_with = ()
                
                # Compare Option 1 and Option 2
                # We want maximum score, then lexicographically smallest indices
                best = best_without
                if score_with > 0:
                    cand = (score_with, indices_with)
                    if cand[0] > best[0]:
                        best = cand
                    elif cand[0] == best[0] and cand[1] < best[1]:
                        best = cand
                
                dp[k][i] = best
        
        # Find the overall best among 1, 2, 3, or 4 intervals
        ans_score = 0
        ans_indices = ()
        for k in range(1, 5):
            score, indices = dp[k][n - 1]
            if score > ans_score:
                ans_score = score
                ans_indices = indices
            elif score == ans_score and indices < ans_indices:
                ans_indices = indices
                
        return list(ans_indices)