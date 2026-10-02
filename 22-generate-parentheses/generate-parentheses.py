class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(current, open_count, close_count):
            # Complete valid combination
            if len(current) == 2 * n:
                res.append("".join(current))
                return

            # Add opening bracket
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()

            # Add closing bracket
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return res
        