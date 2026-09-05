class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # Precompute suffix minimums: suf_min[i] = min(nums[i..n-1])
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])
        
        # Traverse from left to right, maintaining prefix maximum
        pref_max = nums[0]
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            if pref_max - suf_min[i] <= k:
                return i
        
        return -1