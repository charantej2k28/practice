from collections import Counter

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        freq = Counter(digits)
        count = 0
        
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            cand_freq = Counter([d1, d2, d3])
            
            if all(cand_freq[d] <= freq[d] for d in cand_freq):
                count += 1
                
        return count