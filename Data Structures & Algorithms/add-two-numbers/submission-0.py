# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = 0
        dummy = res = ListNode()

        while l1 or l2 or prev:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            curr = l1_val + l2_val + prev
            prev = curr // 10
            curr = curr % 10

            res.next = ListNode(curr)
            res = res.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

