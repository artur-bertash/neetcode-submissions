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
        if not l or l == 1:
            return None

        c, curr = l - n -1 , head

        while c:
            curr = curr.next
            c -=1 
        curr.next = curr.next.next
        return head

