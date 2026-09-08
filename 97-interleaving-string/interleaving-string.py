class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)

        if n + m != len(s3):
            return False

        # Ensure s2 is the shorter string to optimize space to O(min(len(s1), len(s2)))
        if m > n:
            s1, s2 = s2, s1
            n, m = m, n

        # dp[j] indicates if s1[0...i-1] and s2[0...j-1] can interleave to form s3[0...i+j-1]
        dp = [False] * (m + 1)
        dp[0] = True

        # Base case: using only characters from s2 (i = 0)
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Iterate over characters of s1
        for i in range(1, n + 1):
            # Update dp[0] for current row (using only s1 up to index i)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, m + 1):
                # Transition: can reach state from (i - 1, j) or (i, j - 1)
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = from_s1 or from_s2

        return dp[m]