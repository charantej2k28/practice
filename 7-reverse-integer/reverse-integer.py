class Solution(object):

    def reverse(self, x):
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if res > (MAX_INT - digit) // 10:
                return 0

            res = res * 10 + digit

        res *= sign
        if res < MIN_INT or res > MAX_INT:
            return 0

        return res