class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0

        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2 = 1  # Base case: empty string has 1 way
        prev1 = 1  # Base case: string of length 1 (since s[0] != '0')

        for i in range(1, len(s)):
            current = 0

            # Check single-digit decode
            if s[i] != "0":
                current += prev1

            # Check two-digit decode
            two_digit = int(s[i - 1 : i + 1])
            if 10 <= two_digit <= 26:
                current += prev2

            # Update variables for next position
            prev2 = prev1
            prev1 = current

        return prev1
        