# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        cnode = left_tail = head
        idx = 1

        while idx < left:
            left_tail = cnode
            cnode = cnode.next
            idx+=1

        rev_tail = right_head = prev_node = cnode

        while idx <= right:
            cnode = right_head
            right_head = right_head.next
            cnode.next = prev_node
            prev_node = cnode
            idx+=1

        if left>1:
            left_tail.next = cnode
        else:
            head = cnode

        rev_tail.next = right_head

        return head


    def reverseBetween_optimized(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head

        head = ListNode(0,head)
        left_tail = head

        for _ in range(left-1):
            left_tail = left_tail.next

        rev_tail = left_tail.next
        right_head = rev_tail.next

        for _ in range(right-left):
            rev_tail.next = right_head.next
            right_head.next = left_tail.next
            left_tail.next = right_head
            right_head = rev_tail.next
            
        return head.next