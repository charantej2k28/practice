from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

  def zigzagLevelOrder(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    if not root:
      return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
      level_size = len(queue)
      # Use a deque for the current level to append to either end in O(1)
      current_level = deque()

      for _ in range(level_size):
        node = queue.popleft()

        if left_to_right:
          current_level.append(node.val)
        else:
          current_level.appendleft(node.val)

        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)

      result.append(list(current_level))
      left_to_right = not left_to_right

    return result