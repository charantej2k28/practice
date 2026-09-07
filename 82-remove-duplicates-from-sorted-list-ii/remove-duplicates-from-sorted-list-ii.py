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
    dummy = ListNode(0, head)
    prev = dummy

    curr = head
    while curr:
      # Check if curr is the start of a duplicate sequence
      if curr.next and curr.val == curr.next.val:
        # Move curr forward to skip all nodes with this duplicate value
        while curr.next and curr.val == curr.next.val:
          curr = curr.next
        # Link prev past all duplicates
        prev.next = curr.next
      else:
        # No duplicates for curr; advance prev
        prev = prev.next

      curr = curr.next

    return dummy.next