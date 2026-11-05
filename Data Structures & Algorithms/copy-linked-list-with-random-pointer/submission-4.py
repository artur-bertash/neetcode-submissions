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


        oldToNew = defaultdict(lambda: Node(0)) 
        cur = head

        while cur: 
            newNode = oldToNew[cur]
            newNode.val = cur.val
            newNode.next = oldToNew[cur.next] if cur.next else None
            newNode.random = oldToNew[cur.random] if cur.random else None
            cur = cur.next
        return oldToNew[head]

        