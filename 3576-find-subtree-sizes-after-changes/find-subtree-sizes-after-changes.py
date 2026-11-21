
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        ans = [1] * n
        # Tracks the closest ancestor on the current DFS path for each letter 'a'-'z'
        last_seen = [-1] * 26
        
        def dfs(u: int) -> None:
            char_idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[char_idx]
            
            # Determine new parent (if a matching ancestor exists, use it; else keep original)
            new_parent = prev_ancestor if prev_ancestor != -1 else parent[u]
            
            # Update closest ancestor for s[u] before visiting children
            last_seen[char_idx] = u
            
            for v in adj[u]:
                dfs(v)
                
            # Backtrack last_seen when exiting u's subtree
            last_seen[char_idx] = prev_ancestor
            
            # Propagate u's final subtree size up to its new parent
            if new_parent != -1:
                ans[new_parent] += ans[u]
                
        dfs(0)
        return ans