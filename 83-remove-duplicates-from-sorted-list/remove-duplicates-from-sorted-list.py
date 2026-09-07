# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

  def deleteDuplicates(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    curr = head

    while curr and curr.next:
      if curr.val == curr.next.val:
        # Skip the duplicate node
        curr.next = curr.next.next
      else:
        # Advance pointer only when no duplicate is found
        curr = curr.next

    return head