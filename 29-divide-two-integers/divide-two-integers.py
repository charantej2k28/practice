class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # Handle 32-bit signed integer overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine if the result will be negative
        is_negative = (dividend < 0) ^ (divisor < 0)

        # Convert to positive integers
        dvd, dvs = abs(dividend), abs(divisor)
        quotient = 0

        # Subtract largest shifted divisor multiples
        while dvd >= dvs:
            temp_dvs = dvs
            multiple = 1
            while dvd >= (temp_dvs << 1):
                temp_dvs <<= 1
                multiple <<= 1

            dvd -= temp_dvs
            quotient += multiple

        if is_negative:
            quotient = -quotient

        return max(INT_MIN, min(INT_MAX, quotient))