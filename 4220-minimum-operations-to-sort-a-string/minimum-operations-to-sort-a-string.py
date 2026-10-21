class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == ''.join(sorted(s)):
            return 0

        n = len(s)

        # If the string has only two characters,
        # the entire string cannot be selected.
        if n == 2:
            return -1

        # Check whether all characters are identical.
        if len(set(s)) == 1:
            return 0

        # Check whether one operation is sufficient.
        if s[0] == min(s) or s[-1] == max(s):
            return 1

        # If the minimum character is at the end
        # or the maximum character is at the beginning,
        # two operations may be enough.
        if s[0] == max(s) and s[-1] == min(s):
            if s.count(s[0]) == 1 and s.count(s[-1]) == 1:
                return 3

        return 2