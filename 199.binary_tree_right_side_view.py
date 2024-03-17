class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        stack = [(root, 1)]
        right_side = []

        while stack:
            cnode, level = stack.pop()
            if level > len(right_side):
                right_side.append(cnode.val)
            if cnode.left:
                stack.append((cnode.left, level+1))
            if cnode.right:
                stack.append((cnode.right, level+1))
        
        return right_side