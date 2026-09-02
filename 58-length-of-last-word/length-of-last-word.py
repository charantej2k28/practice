class Solution(object):

  def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    length = 0
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == " ":
      i -= 1

    # Count the characters of the last word
    while i >= 0 and s[i] != " ":
      length += 1
      i -= 1

    return length