
import java.util.*;

class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.length;
        Deque<long[]> dq = new ArrayDeque<>();

        long ans = 0;
        long cost = 0;
        int j = n - 1;

        for (int i = n - 1; i >= 0; i--) {
            int count = 1;

            while (!dq.isEmpty() && dq.peekLast()[0] < nums[i]) {
                long[] p = dq.removeLast();
                count += p[1];
                cost += (nums[i] - p[0]) * p[1];
            }

            dq.addLast(new long[]{nums[i], count});

            while (cost > k) {
                long[] p = dq.removeFirst();

                cost -= p[0] - nums[j];
                j--;

                if (p[1] > 1) {
                    dq.addFirst(new long[]{p[0], p[1] - 1});
                }
            }

            ans += j - i + 1;
        }

        return ans;
    }
}
