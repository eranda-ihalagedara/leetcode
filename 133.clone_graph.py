class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = [node]
        nodes = {node:Node(node.val)}

        while queue:
            nd = queue.pop()
            for nr in nd.neighbors:
                if nr not in nodes:
                    nodes[nr] = Node(nr.val)
                    queue.append(nr)
                nodes[nd].neighbors.append(nodes[nr])

        return nodes[node]