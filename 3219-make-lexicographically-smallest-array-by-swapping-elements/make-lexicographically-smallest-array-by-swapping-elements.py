class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        # Pair each value with its original index and sort by value
        sorted_pairs = sorted((val, i) for i, val in enumerate(nums))
        
        res = [0] * n
        i = 0
        
        while i < n:
            j = i + 1
            # Find the boundary of the current connected component
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1
            
            # Extract and sort the indices for this group
            indices = sorted(sorted_pairs[k][1] for k in range(i, j))
            
            # Place the sorted values into the sorted indices
            for k in range(i, j):
                res[indices[k - i]] = sorted_pairs[k][0]
            
            i = j
            
        return res