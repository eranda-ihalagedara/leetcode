# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        values = set()
        duplicates = set()
        pre_node = cnode = head
        
        while cnode:
            if cnode.val in values:
                pre_node.next = cnode.next
                duplicates.add(cnode.val)
            else:
                pre_node = cnode
                values.add(cnode.val)
            cnode = cnode.next
        
        if head.val in duplicates:
            head = head.next
        cnode = head
        head = pre_node = ListNode(0,head)
        
        while cnode:
            if cnode.val in duplicates:
                pre_node.next = cnode.next
            else:
                pre_node = cnode
            cnode = cnode.next

        return head.next


    def deleteDuplicates_optimized_I(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        elif not head.next:
            return head

        pre_node = head = ListNode(0,head)
        cnode = head.next

        while cnode:
            
            if cnode.next and cnode.next.val == cnode.val:
                while cnode.next and cnode.val==cnode.next.val:
                    cnode = cnode.next
                pre_node.next = cnode.next
            else:
                pre_node = pre_node.next
            
            cnode = cnode.next

        return head.next