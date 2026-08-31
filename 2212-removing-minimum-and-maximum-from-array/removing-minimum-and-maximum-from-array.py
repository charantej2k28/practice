class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)

        delete_both_front = j + 1
        delete_both_back = n - i
        delete_both_ends = (i + 1) + (n - j)

        return min(delete_both_front, delete_both_back, delete_both_ends)