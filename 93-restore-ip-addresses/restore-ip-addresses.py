class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        # A valid IPv4 string must have between 4 and 12 digits
        if len(s) < 4 or len(s) > 12:
            return res

        def backtrack(start, segments):
            # If we have 4 segments and have used all characters
            if len(segments) == 4:
                if start == len(s):
                    res.append(".".join(segments))
                return

            # Prune if remaining characters cannot fit into remaining segments
            remaining_segments = 4 - len(segments)
            remaining_chars = len(s) - start
            if not (remaining_segments <= remaining_chars <= remaining_segments * 3):
                return

            # Each segment can be 1, 2, or 3 digits long
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start : start + length]

                # Check for leading zero
                if len(part) > 1 and part[0] == "0":
                    break

                # Check numerical value range [0, 255]
                if int(part) <= 255:
                    backtrack(start + length, segments + [part])

        backtrack(0, [])
        return res