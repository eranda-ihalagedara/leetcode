class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        stack = [root]
        zigzag_order = []
        order = 1

        while stack:
            stack_buffer = []
            zigzag_buffer = []
            
            for cnode in stack:
                zigzag_buffer.append(cnode.val)
                if cnode.left:
                    stack_buffer.append(cnode.left)
                if cnode.right:
                    stack_buffer.append(cnode.right)
            
            if order < 0:
                zigzag_buffer.reverse()
            
            zigzag_order.append(zigzag_buffer)
            stack = stack_buffer
            order *= -1
        
        return zigzag_order


    def zigzagLevelOrder_optimized(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        que = deque([root])
        zigzag_order = []
        order = 1

        while que:
            zigzag_buffer = []
            for i in range(len(que)):
                cnode = que.popleft()
                zigzag_buffer.append(cnode.val)
                if cnode.left: que.append(cnode.left)
                if cnode.right: que.append(cnode.right)

            zigzag_order.append(zigzag_buffer[::order])
            order *= -1
        
        return zigzag_order