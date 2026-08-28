from collections import Counter

class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        m = n // 2
        counts = Counter(s)
        
        odd_chars = [ch for ch, freq in counts.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {ch: counts[ch] // 2 for ch in counts if counts[ch] // 2 > 0}
        
        def build_palindrome(half_str):
            rev_half = half_str[::-1]
            if n % 2 != 0:
                return half_str + mid_char + rev_half
            return half_str + rev_half

        best_candidate = None

        # Case 1: First half matches target[:m] exactly
        cur_counts = dict(half_counts)
        possible_prefix = []
        can_match_prefix = True
        
        for ch in target[:m]:
            if cur_counts.get(ch, 0) > 0:
                cur_counts[ch] -= 1
                possible_prefix.append(ch)
            else:
                can_match_prefix = False
                break
                
        if can_match_prefix:
            cand = build_palindrome("".join(possible_prefix))
            if cand > target:
                best_candidate = cand

        # Case 2: Diverge at index i (0 <= i < m) with P[i] > target[i]
        # We iterate from right to left (deepest prefix) to find minimal larger options
        for i in range(m - 1, -1, -1):
            # Tally counts used by target[0...i-1]
            prefix_counts = Counter(target[:i])
            
            # Check if target[:i] is formable
            if any(prefix_counts[ch] > half_counts.get(ch, 0) for ch in prefix_counts):
                continue
                
            rem_counts = {ch: half_counts.get(ch, 0) - prefix_counts[ch] for ch in half_counts}
            
            # Find the smallest character c > target[i] available
            available_chars = sorted([ch for ch, cnt in rem_counts.items() if cnt > 0 and ch > target[i]])
            
            if available_chars:
                chosen_ch = available_chars[0]
                rem_counts[chosen_ch] -= 1
                
                # Fill the rest with smallest remaining characters
                rest = "".join(sorted([ch * rem_counts[ch] for ch in rem_counts if rem_counts[ch] > 0]))
                first_half = target[:i] + chosen_ch + rest
                cand = build_palindrome(first_half)
                
                if best_candidate is None or cand < best_candidate:
                    best_candidate = cand

        return best_candidate if best_candidate is not None else ""