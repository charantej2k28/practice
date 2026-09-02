class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        all_cols = (1 << n) - 1

        def backtrack(row, cols, diag1, diag2):
            if row == n:
                self.count += 1
                return

            # Available positions for this row are bits that are 0 in cols, diag1, and diag2
            available_positions = all_cols & ~(cols | diag1 | diag2)

            while available_positions:
                # Pick the lowest set bit (rightmost valid column)
                col_bit = available_positions & -available_positions
                # Clear that bit from available positions
                available_positions &= available_positions - 1

                # Recurse to the next row, shifting diagonal masks accordingly
                backtrack(
                    row + 1,
                    cols | col_bit,
                    (diag1 | col_bit) << 1,
                    (diag2 | col_bit) >> 1,
                )

        backtrack(0, 0, 0, 0)
        return self.count