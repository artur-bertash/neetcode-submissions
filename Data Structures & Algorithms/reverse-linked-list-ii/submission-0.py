# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        dummy = ListNode(0, head)
        leftPrev = dummy

        while i < left:
            leftPrev = leftPrev.next
            i += 1
        
        cur = leftPrev.next
        prev = None
        while cur and i <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            i += 1

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next


