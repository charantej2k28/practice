# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None
        curr = root

        # Morris In-order Traversal
        while curr:
            if not curr.left:
                # Process curr node
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find the in-order predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    # Create a temporary thread to current node
                    pred.right = curr
                    curr = curr.left
                else:
                    # Revert the temporary thread
                    pred.right = None
                    # Process curr node
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        # Swap the values of the two erroneous nodes
        if first and second:
            first.val, second.val = second.val, first.val