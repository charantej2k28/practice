
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        maximum = left
        remaining = k - sum(max(0, d - maximum) for d in diff)

        result = 0
        for d in diff:
            reduced = min(d, maximum)
            result += reduced * reduced

        # Reduce remaining differences by one more where possible
        result -= remaining * (2 * maximum - 1)

        return result
