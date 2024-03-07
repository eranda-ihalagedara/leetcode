# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        return self.msort(head)

    def partition(self, head):
        if not head or not head.next:
            return head, None

        slow = fast =  pre_node = head
        while fast and fast.next:
            pre_node = slow
            slow = slow.next
            fast = fast.next.next

        right_head = pre_node.next
        pre_node.next = None

        return head, right_head
    
    def merge(self, left, right):
        head = tail = ListNode(0)

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        elif right:
            tail.next = right
        
        return head.next

    def msort(self, head):
        if not head or not head.next:
            return head
        
        left_head,right_head = self.partition(head)

        left_head = self.msort(left_head)
        right_head = self.msort(right_head)

        return self.merge(left_head, right_head)

        
