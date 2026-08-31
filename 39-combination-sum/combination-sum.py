class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def backtrack(remain, combo, start):
            if remain == 0:
                result.append(list(combo))
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remain:
                    break

                combo.append(num)
                backtrack(remain - num, combo, i)
                combo.pop()

        backtrack(target, [], 0)
        return result