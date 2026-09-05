class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # dp[j] represents the edit distance between word1 prefix and word2[:j]
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(
                        dp[j],      # Deletion
                        dp[j - 1],  # Insertion
                        prev        # Replacement
                    )
                prev = temp
                
        return dp[n]
        