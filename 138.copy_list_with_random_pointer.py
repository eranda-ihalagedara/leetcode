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
        
        if not head:
            return head
        
        cnode = head
        node_copy = head_copy = Node(0)
        node_map = dict()

        while cnode:
            node_copy.next = Node(cnode.val)
            node_copy = node_copy.next
            node_map[cnode] = node_copy
            cnode = cnode.next
        
        cnode = head
        node_copy = head_copy = head_copy.next
        
        while cnode:
            if cnode.random:
                node_copy.random = node_map[cnode.random]
            cnode = cnode.next
            node_copy = node_copy.next

        return head_copy


    def copyRandomList_optimized(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        
        cnode = head
        node_map = dict()

        while cnode:
            node_copy = Node(cnode.val)
            node_map[cnode] = node_copy
            cnode = cnode.next
        
        cnode = head

        while cnode:
            node_copy = node_map[cnode]
            node_copy.next = node_map[cnode.next] if cnode.next else None
            node_copy.random = node_map[cnode.random] if cnode.random else None

            cnode = cnode.next

        return node_map[head]

