class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        dummy = ListNode(0, head)
        leftPrev = dummy

        for _ in range(left - 1):
            leftPrev = leftPrev.next


        
        cur = leftPrev.next
        prev = None
        i = left
        while cur and i <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            i += 1

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next

