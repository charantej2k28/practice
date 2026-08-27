class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        # dp[i][j] represents if s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[m][n] = True
        
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = (i < m) and (p[j] == s[i] or p[j] == '.')
                
                if j + 1 < n and p[j + 1] == '*':
                    # Choice 1: Use '*' as 0 occurrences -> dp[i][j + 2]
                    # Choice 2: Use '*' as 1+ occurrences -> dp[i + 1][j] (if first char matches)
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
                    
        return dp[0][0]