class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        # Track occupied columns and diagonals
        cols = set()
        pos_diags = set()  # (row + col)
        neg_diags = set()  # (row - col)

        # board[row] will store the column index of the queen at that row
        board = [-1] * n

        def backtrack(row):
            if row == n:
                # Construct the board representation from queen placements
                solution = []
                for r in range(n):
                    c = board[r]
                    solution.append("." * c + "Q" + "." * (n - c - 1))
                solutions.append(solution)
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
                    continue

                # Place queen
                board[row] = col
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack / Remove queen
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)

        backtrack(0)
        return solutions