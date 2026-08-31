class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"

        for _ in range(n - 1):
            next_seq = []
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                next_seq.append(str(count))
                next_seq.append(result[i])
                i += 1
            result = "".join(next_seq)

        return result