# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val> list2.val:
            list1, list2 = list2, list1
        
        p1, p2 = list1, list2

        while p1.next is not None and p2 is not None :
            if p2.val < p1.next.val:
                if p2.next is not None:
                    p2_temp = p2.next
                    p2.next = p1.next
                    p1.next = p2
                    p2 = p2_temp
                    
                else:
                    p2.next = p1.next
                    p1.next = p2
                    return list1

            p1 = p1.next
        
        if p1.next is None:
            p1.next = p2

        return list1
		
	def mergeTwoLists_optimized(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = curr = ListNode(0)

        while list1 is not None and list2 is not None :
            
            if list1.val < list2.val:

                curr.next = list1
                list1 = list1.next
                    
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        curr.next = list1 or list2

        return head.next
		
		
    
	def mergeTwoLists_recursion(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
        