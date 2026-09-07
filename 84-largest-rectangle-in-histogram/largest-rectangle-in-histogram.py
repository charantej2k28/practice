class Solution(object):

  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    stack = []
    max_area = 0
    # Append a sentinel 0 to pop all remaining elements in the stack at the end
    extended_heights = heights + [0]

    for i, h in enumerate(extended_heights):
      while stack and h < extended_heights[stack[-1]]:
        height = extended_heights[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, height * width)
      stack.append(i)

    return max_area