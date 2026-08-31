class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    digit = int(board[r][c])
                    mask = 1 << digit
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask

        def backtrack(k):
            if k == len(empty):
                return True

            r, c = empty[k]
            box_idx = (r // 3) * 3 + (c // 3)

            for d in range(1, 10):
                mask = 1 << d
                if not (rows[r] & mask or cols[c] & mask or boxes[box_idx] & mask):
                    board[r][c] = str(d)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask

                    if backtrack(k + 1):
                        return True

                    board[r][c] = '.'
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[box_idx] &= ~mask

            return False

        backtrack(0)
        