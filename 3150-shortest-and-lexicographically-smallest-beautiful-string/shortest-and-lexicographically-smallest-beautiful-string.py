class Solution:
    def shortestBeautifulSubstring(self, s, k):
        left = 0
        ones = 0
        min_len = float('inf')
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones == k:
                curr = s[left:right + 1]

                if len(curr) < min_len:
                    min_len = len(curr)
                    ans = curr
                elif len(curr) == min_len and curr < ans:
                    ans = curr

                if s[left] == '1':
                    ones -= 1

                left += 1

        return ans