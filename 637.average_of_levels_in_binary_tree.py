# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []
        
        lcount = {}
        lavg = {}
        node_stack = [[root,1]]

        while node_stack:
            node, level = node_stack.pop(0)

            n = lcount.get(level, 0)
            lavg[level] = (lavg.get(level,0) * n + node.val)/(n+1)
            lcount[level] = n+1

            if node.left:
                node_stack.append([node.left, level+1])
            if node.right:
                node_stack.append([node.right, level+1])
        
        return [x for x in lavg.values()]
		
	def averageOfLevels_optimized(self, root: Optional[TreeNode]) -> List[float]:
        
        node_queue, avgs = [root], []

        while node_queue:
            lsum = 0
            qlen = len(node_queue)
            for i in range(qlen):
                node = node_queue.pop(0)
                lsum += node.val

                if node.left:
                    node_queue.append(node.left)
                
                if node.right:
                    node_queue.append(node.right)
                
            avgs.append(lsum/qlen)

        return avgs

