# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        stack = []
        cnode = root
        
        while stack or cnode:
            if cnode:
                stack.append(cnode)
                cnode = cnode.right
            else:
                cnode = stack.pop()
                self.inorder.append(cnode.val)
                cnode = cnode.left

        self.idx = len(self.inorder)

    def next(self) -> int:
        self.idx-=1
        return self.inorder[self.idx]

    def hasNext(self) -> bool:
        return self.idx > 0



class BSTIterator_optimized:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        cnode = root
        
        while cnode:
            self.stack.append(cnode)
            cnode = cnode.left

    def next(self) -> int:
        cnode = self.stack.pop()
        nxt_val = cnode.val
        cnode = cnode.right
        while cnode:
            self.stack.append(cnode)
            cnode = cnode.left
        return nxt_val

    def hasNext(self) -> bool:
        return len(self.stack) > 0