# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(head, n):
            if not head:
                return 0
            dist = rec(head.next, n) + 1 
            if dist == n + 1:
                head.next = head.next.next
            return dist
        if rec(head, n) == n:
            return head.next
        return head
