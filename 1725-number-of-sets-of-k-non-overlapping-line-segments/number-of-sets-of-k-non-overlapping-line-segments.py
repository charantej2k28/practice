class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        total_n = n + k - 1
        total_r = 2 * k

        if total_r > total_n:
            return 0

        # C(N, R) = N! / (R! * (N - R)!)
        # Optimize by using the smaller symmetry: C(N, R) == C(N, N - R)
        total_r = min(total_r, total_n - total_r)

        ans = 1
        for i in range(1, total_r + 1):
            ans = ans * (total_n - i + 1) // i

        return ans % MOD