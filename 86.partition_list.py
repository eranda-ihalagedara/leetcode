# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or x <= -100:
            return head

        right_head = cnode = head
        head = left_tail = ListNode(0, head)

        while right_head and right_head.val < x :
            right_head = right_head.next
            left_tail = left_tail.next
        
        if not right_head:
            return head.next

        cnode =  right_head

        while cnode.next:
            if cnode.next.val < x:
                left_tail.next = cnode.next
                left_tail = left_tail.next
                cnode.next = cnode.next.next
                left_tail.next = right_head
            else:
                cnode = cnode.next

        return head.next
		

    def partition_optimized(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head or not head.next or x <= -100:
            return head

        right_head = right_tail = ListNode(0)
        left_head = left_tail = ListNode(0)

        while head :
            if head.val < x:
                left_tail.next = head
				left_tail = left_tail.next
            else:
                right_tail.next = head
				right_tail = right_tail.next
            
            head = head.next
        
        left_tail.next = right_head.next
        right_tail.next = None

        return left_head.next