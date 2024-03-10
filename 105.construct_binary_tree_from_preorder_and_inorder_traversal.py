# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(inorder) == 1:
            return root

        rid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:rid+1], inorder[:rid])
        root.right = self.buildTree(preorder[rid+1:], inorder[rid+1:])

        return root



    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder) == 1:
            return TreeNode(preorder[0])

        inorder_index = {n:i for i, n in enumerate(inorder)}

        def builder(preorder: List[int], inorder: List[int], left, right, pre_id):
            if right < left:
                return None
            
            root = TreeNode(preorder[pre_id])

            if left == right:
                return root
            
            root_id = inorder_index[preorder[pre_id]]

            root.left = builder(preorder, inorder, left, root_id-1, pre_id+1)
            root.right = builder(preorder, inorder, root_id+1, right, pre_id+root_id-left+1)

            return root

        return builder(preorder, inorder, 0, len(preorder)-1, 0)