class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                if num > remain:
                    break

                combo.append(num)
                backtrack(remain - num, combo, i + 1)
                combo.pop()

        backtrack(target, [], 0)
        return result