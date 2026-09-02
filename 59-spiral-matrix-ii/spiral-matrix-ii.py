class Solution(object):

  def generateMatrix(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    matrix = [[0] * n for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    val = 1

    while top <= bottom and left <= right:
      # Traverse left to right along top row
      for col in range(left, right + 1):
        matrix[top][col] = val
        val += 1
      top += 1

      # Traverse top to bottom along right column
      for row in range(top, bottom + 1):
        matrix[row][right] = val
        val += 1
      right -= 1

      # Traverse right to left along bottom row
      if top <= bottom:
        for col in range(right, left - 1, -1):
          matrix[bottom][col] = val
          val += 1
        bottom -= 1

      # Traverse bottom to top along left column
      if left <= right:
        for row in range(bottom, top - 1, -1):
          matrix[row][left] = val
          val += 1
        left += 1

    return matrix