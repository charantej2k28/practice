class Solution(object):

  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    max_reach = 0
    n = len(nums)

    for i in range(n):
      # If current position cannot be reached
      if i > max_reach:
        return False

      # Update the furthest position reachable
      max_reach = max(max_reach, i + nums[i])

      # Early exit if we can already reach or surpass the last index
      if max_reach >= n - 1:
        return True

    return True