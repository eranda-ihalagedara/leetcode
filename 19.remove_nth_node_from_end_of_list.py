# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnode = head
        n+=1
        buffer = dict()
        i = 0
        while cnode:
            buffer[i%n] = cnode
            cnode = cnode.next
            i+=1

        if i == n-1:
            return head.next

        buffer[i%n].next = buffer[i%n].next.next

        return head


    def removeNthFromEnd_optimized(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lnode = rnode = head
        for _ in range(n): rnode = rnode.next
        
        if not rnode: return head.next

        while rnode.next:
            lnode, rnode = lnode.next, rnode.next

        lnode.next = lnode.next.next

        return head