class Solution(object):

  def distinctSubseqII(self, s):
    """
    :type s: str
    :rtype: int
    """
    MOD = 10**9 + 7
    # ends_with[c] stores the count of distinct subsequences ending with character c
    ends_with = [0] * 26

    for char in s:
      idx = ord(char) - ord("a")
      # New count for subsequences ending with `char` is 1 (the single char subsequence)
      # plus all existing distinct subsequences appended with `char`
      ends_with[idx] = (sum(ends_with) + 1) % MOD

    return sum(ends_with) % MOD