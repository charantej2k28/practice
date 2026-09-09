# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

  def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: Optional[TreeNode]
    """
    # Map each value to its index in the inorder traversal for O(1) lookups
    inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
    self.pre_idx = 0

    def helper(in_left, in_right):
      if in_left > in_right:
        return None

      # The current root is always the next unused element in preorder
      root_val = preorder[self.pre_idx]
      self.pre_idx += 1
      root = TreeNode(root_val)

      # Elements to the left of root_idx in inorder belong to the left subtree
      root_idx = inorder_index_map[root_val]

      # Build left and right subtrees (left must be built first to match preorder sequence)
      root.left = helper(in_left, root_idx - 1)
      root.right = helper(root_idx + 1, in_right)

      return root

    return helper(0, len(inorder) - 1)