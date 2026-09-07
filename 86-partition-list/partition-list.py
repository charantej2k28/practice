# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

  def partition(self, head, x):
    """
    :type head: Optional[ListNode]
    :type x: int
    :rtype: Optional[ListNode]
    """
    # Create two dummy heads to maintain two separate lists:
    # one for nodes < x, and one for nodes >= x
    less_head = ListNode(0)
    greater_head = ListNode(0)

    less = less_head
    greater = greater_head

    curr = head
    while curr:
      if curr.val < x:
        less.next = curr
        less = less.next
      else:
        greater.next = curr
        greater = greater.next
      curr = curr.next

    # Terminate the greater list to prevent cycles
    greater.next = None
    # Connect the less list with the greater list
    less.next = greater_head.next

    return less_head.next