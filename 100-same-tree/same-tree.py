# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Both are empty
        if not p and not q:
            return True

        # One is empty and the other is not
        if not p or not q:
            return False

        # Values must match and both subtrees must be identical
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(
            p.right, q.right
        )