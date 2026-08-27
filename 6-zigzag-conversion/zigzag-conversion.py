class Solution(object):

    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        curr_row = 0
        step = -1

        for char in s:
            rows[curr_row].append(char)
            if curr_row == 0 or curr_row == numRows - 1:
                step = -step
            curr_row += step

        return "".join("".join(row) for row in rows)