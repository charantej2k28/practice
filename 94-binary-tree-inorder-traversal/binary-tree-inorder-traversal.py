# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        stack = []
        curr = root

        while curr or stack:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # Current must be None at this point, pop from stack
            curr = stack.pop()
            res.append(curr.val)

            # We have visited the node and its left subtree; now visit the right subtree
            curr = curr.right

        return res