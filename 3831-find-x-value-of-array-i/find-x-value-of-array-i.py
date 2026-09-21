class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k

        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            val = num % k
            new_dp = [0] * k

            # Start a new subarray with just nums[i]
            new_dp[val] += 1

            # Extend every subarray ending at the previous position
            for r in range(k):
                if dp[r]:
                    new_r = (r * val) % k
                    new_dp[new_r] += dp[r]

            # All subarrays ending here contribute to the answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans