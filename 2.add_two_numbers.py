# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Head created with default node & input lists current point stored
        head = cnode = ListNode()

        # Carry for sum
        carry = 0

        while l1 or l2:
            v1, v2 = 0,0

            if l1:
                v1 = l1.val
                l1 = l1.next
            
            if l2:
                v2 = l2.val
                l2 = l2.next

            sum = v1 + v2 + carry

            carry = sum // 10
            
            cnode.next = ListNode(sum%10)
            cnode = cnode.next
        
        if carry == 1:
            cnode.next = ListNode(1)

        # Dropping first default node
        return head.next


    def addTwoNumbers_optimizedI(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # input lists current point stored
        head = cnode = cnode_prev = l1

        # Carry for sum
        carry = 0

        while cnode:
            
            cnode.val += carry

            if l2:
                cnode.val += l2.val
                l2 = l2.next

            carry = cnode.val // 10
            cnode.val = cnode.val%10
            
            cnode_prev = cnode
            cnode = cnode.next


        cnode  = cnode_prev.next = l2
  
        while cnode and carry:
            
            cnode.val += carry

            carry = cnode.val // 10
            cnode.val = cnode.val%10

            cnode_prev = cnode
            cnode = cnode.next

        if carry:
            cnode_prev.next = ListNode(1)

        return head