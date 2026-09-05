from collections import Counter

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        
        # Pruning 1: Length check
        if len(word) > m * n:
            return False
            
        # Pruning 2: Character frequency count
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
                
        # Pruning 3: Reverse word if the tail character is rarer than the head
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False
            
            # Mark cell as visited in-place
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore 4-directional neighbors
            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))
            
            # Backtrack
            board[r][c] = temp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
                    
        return False