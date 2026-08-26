from collections import Counter

class Solution(object):
    def checkStrings(self, s1, s2):
        even1 = Counter(s1[0::2])
        even2 = Counter(s2[0::2])

        odd1 = Counter(s1[1::2])
        odd2 = Counter(s2[1::2])

        return even1 == even2 and odd1 == odd2