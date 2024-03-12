# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        root = TreeNode(postorder[-1])
        if len(inorder) == 1:
            return root
        root_id = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:root_id], postorder[:root_id])
        root.right = self.buildTree(inorder[root_id+1:], postorder[root_id:-1])

        return root
	
	
	
	
    def buildTree_optimized(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 1:
            return TreeNode(inorder[0])
        self.post_id = len(postorder)-1
        
        inorder_index = {n:i for i, n in enumerate(inorder)}
		
        def builder(left, right):
            if right < left:
                return None
        
            root = TreeNode(postorder[self.post_id])
            self.post_id-=1
            if left == right: return root

            root_id = inorder_index[root.val]
            root.right = builder(root_id+1, right)
            root.left = builder(left, root_id-1)
            
            return root

        return builder(0, len(inorder)-1)	
	
	
	

    def buildTree_optimizedII(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
		inorder_index = {n:i for i, n in enumerate(inorder)}
		
        def builder(left, right, post_id):
            if right < left:
                return None
        
            root = TreeNode(postorder[post_id])
            
            if left == right:
                return root

            root_id = inorder_index[postorder[post_id]]

            root.left = builder(left, root_id-1, root_id-1+post_id-right)
            root.right = builder(root_id+1, right, post_id-1)

            return root

        return builder(0, len(inorder)-1, len(inorder)-1)