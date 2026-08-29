class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp