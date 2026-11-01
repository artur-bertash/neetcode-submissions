"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memo = {}
        def rec(head):
            if not head:
                return None
            if head in memo:
                return memo[head]
            new_node = Node(head.val)
            memo[head] = new_node

            new_node.next = rec(head.next)
            new_node.random = rec(head.random)
            

            return new_node
        return rec(head)