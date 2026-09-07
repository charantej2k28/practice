class Solution(object):

  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
      return 0

    cols = len(matrix[0])
    heights = [0] * (cols + 1)  # Extra 0 as a sentinel to flush the stack
    max_area = 0

    for row in matrix:
      # Update histogram bar heights for the current row
      for j in range(cols):
        heights[j] = heights[j] + 1 if row[j] == "1" else 0

      # Compute largest rectangle area in the current histogram
      stack = []
      for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
          height = heights[stack.pop()]
          width = i if not stack else i - stack[-1] - 1
          max_area = max(max_area, height * width)
        stack.append(i)

    return max_area