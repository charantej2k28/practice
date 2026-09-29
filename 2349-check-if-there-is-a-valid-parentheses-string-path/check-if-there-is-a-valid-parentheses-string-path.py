class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Number of characters in the path must be even
        if (m + n - 1) % 2 == 1:
            return False

        # A valid path cannot start with ')'
        if grid[0][0] == ')':
            return False

        # Maximum possible balance is m + n
        max_balance = m + n

        dp = [[[False] * (max_balance + 1)
               for _ in range(n)]
              for _ in range(m)]

        dp[0][0][1] = True

        for i in range(m):
            for j in range(n):
                for balance in range(max_balance + 1):

                    if not dp[i][j][balance]:
                        continue

                    # Move down
                    if i + 1 < m:
                        if grid[i + 1][j] == '(':
                            nb = balance + 1
                        else:
                            nb = balance - 1

                        if nb >= 0:
                            dp[i + 1][j][nb] = True

                    # Move right
                    if j + 1 < n:
                        if grid[i][j + 1] == '(':
                            nb = balance + 1
                        else:
                            nb = balance - 1

                        if nb >= 0:
                            dp[i][j + 1][nb] = True

        return dp[m - 1][n - 1][0]