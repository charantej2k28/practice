class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_exponent = False
        seen_dot = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in "+-":
                # A sign is only valid at the start or immediately after 'e'/'E'
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char == ".":
                # A dot cannot repeat and cannot appear after an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                # An exponent cannot repeat and must follow at least one digit
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Must see at least one digit after the exponent
            else:
                return False

        # The string is valid only if at least one digit was seen in the final section
        return seen_digit