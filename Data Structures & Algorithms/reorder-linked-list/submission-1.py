# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#0 0 
#1 2
#2 4
#3 6
#4 8
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(st):
            prev = None
            curr = st
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        def merge(h1, h2):
            dummy = res = ListNode()
            while h1 or h2:
                if h1:
                    res.next = h1
                    res = res.next
                    h1 = h1.next
                if h2:
                    res.next = h2
                    res = res.next
                    h2 = h2.next
            return dummy.next

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        s1, s2 = head, slow.next
        slow.next = None 
        s2 = reverse(s2)
        merge(s1, s2)
        
