class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        low = head
        high = head.next

        while high is not None:
            if low == high:
                return True
            elif high.next is None:
                return False

            low = low.next
            high = high.next.next

        return False
		
		
	def hasCycle_optimized(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False
        
        nodes = set()

        while head is not None:
            head = head.next
            if head in nodes:
                return True
            nodes.add(head)

        return False