class Solution(object):

  def isScramble(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    memo = {}

    def dfs(s1, s2):
      if s1 == s2:
        return True
      if (s1, s2) in memo:
        return memo[(s1, s2)]

      # Prune branches where character frequencies don't match
      if sorted(s1) != sorted(s2):
        memo[(s1, s2)] = False
        return False

      n = len(s1)
      for i in range(1, n):
        # Case 1: Without swapping substrings
        # s1[:i] matches s2[:i] and s1[i:] matches s2[i:]
        if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
          memo[(s1, s2)] = True
          return True

        # Case 2: With swapping substrings
        # s1[:i] matches s2[n-i:] and s1[i:] matches s2[:n-i]
        if dfs(s1[:i], s2[n - i :]) and dfs(s1[i:], s2[: n - i]):
          memo[(s1, s2)] = True
          return True

      memo[(s1, s2)] = False
      return False

    return dfs(s1, s2)