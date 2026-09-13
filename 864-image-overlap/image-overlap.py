from collections import defaultdict

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        
        # Collect coordinates of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count occurrences of each shift vector (dr, dc)
        shift_counts = defaultdict(int)
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] += 1
                
        return max(shift_counts.values()) if shift_counts else 0