class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            pal[i][i] = True

        # Check palindromes of length >= 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length == 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum number of valid non-overlapping
        # palindromes using s[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't select a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Try every palindrome ending at i-1
            for start in range(i - k + 1):
                if i - start >= k and pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]