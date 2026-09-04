# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length and the tail node
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # Step 2: Handle redundant rotations
        k = k % n
        if k == 0:
            return head

        # Step 3: Form a circular linked list
        tail.next = head

        # Step 4: Find the node just before the new head (n - k steps)
        steps_to_new_tail = n - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 5: Disconnect the loop and return the new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head