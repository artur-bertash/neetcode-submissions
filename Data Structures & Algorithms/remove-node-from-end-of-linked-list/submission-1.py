# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, curr = 0, head
        while curr:
            curr = curr.next
            l += 1
        
        dummy = ListNode()
        dummy.next = head

        curr = dummy
        i = 0
        while i < l - n:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return dummy.next
        


        

