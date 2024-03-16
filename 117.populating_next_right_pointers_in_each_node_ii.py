class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root

        level_stack = [root]

        while level_stack:
            buffer_stack = []
            for i in range(1,len(level_stack)):
                level_stack[i-1].next = level_stack[i]
                if level_stack[i-1].left:
                    buffer_stack.append(level_stack[i-1].left)
                if level_stack[i-1].right:
                    buffer_stack.append(level_stack[i-1].right)
            
            if level_stack[-1].left:
                buffer_stack.append(level_stack[-1].left)
            if level_stack[-1].right:
                buffer_stack.append(level_stack[-1].right)
            level_stack = buffer_stack

        return root

    def connect_optimized(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        cnode = root
        while cnode:
            tail = head = Node(0)
            while cnode:
                if cnode.left:
                    tail.next = cnode.left
                    tail = tail.next
                if cnode.right:
                    tail.next = cnode.right
                    tail = tail.next
                
                cnode = cnode.next
            cnode = head.next
        
        return root