# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0 or not head:
            return head

        rnode = lnode = head

        sz = 1
        for _ in range(k):
            if rnode.next:
                rnode = rnode.next
                sz +=1
            else:
                break
        
        if not rnode.next:
            k=k%sz
            for _ in range(sz-k-1):
                lnode = lnode.next
            
        else:
            while rnode.next:
                rnode = rnode.next
                lnode = lnode.next
        
        rnode.next = head
        head = lnode.next
        lnode.next = None

        return head

        
