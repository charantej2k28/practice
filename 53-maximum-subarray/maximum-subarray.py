class Solution(object):

  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    current_sum = nums[0]

    for x in nums[1:]:
      # Either extend the previous subarray or start a new one from x
      current_sum = max(x, current_sum + x)
      max_sum = max(max_sum, current_sum)

    return max_sum