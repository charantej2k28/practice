from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        required = len(need)
        
        window = {}
        matched = 0
        
        min_len = float('inf')
        best_left = 0
        left = 0
        
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                matched += 1
            
            # Shrink window from the left as long as it's valid
            while matched == required:
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    best_left = left
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    matched -= 1
                
                left += 1
                
        return "" if min_len == float('inf') else s[best_left:best_left + min_len]