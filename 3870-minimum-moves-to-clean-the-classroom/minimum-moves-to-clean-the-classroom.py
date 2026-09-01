from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m, n = len(classroom), len(classroom[0])
        litter_map = {}
        start = None
        
        # Identify start position and assign bit indexes to litter cells
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start = (r, c)
                elif cell == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        num_litters = len(litter_map)
        target_mask = (1 << num_litters) - 1
        
        if target_mask == 0:
            return 0
            
        # best_energy[r][c][mask] stores the maximum energy seen at that state
        best_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        sr, sc = start
        initial_mask = 0
        
        # Queue stores: (r, c, mask, energy_left, moves)
        queue = deque([(sr, sc, initial_mask, energy, 0)])
        best_energy[sr][sc][initial_mask] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_energy, moves = queue.popleft()
            
            if mask == target_mask:
                return moves
                
            if cur_energy == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    next_energy = cur_energy - 1
                    next_mask = mask
                    
                    if cell == 'R':
                        next_energy = energy
                    elif cell == 'L' and (nr, nc) in litter_map:
                        next_mask = mask | (1 << litter_map[(nr, nc)])
                    
                    # Only proceed if this path brings strictly higher remaining energy
                    if next_energy > best_energy[nr][nc][next_mask]:
                        best_energy[nr][nc][next_mask] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, moves + 1))
                        
        return -1