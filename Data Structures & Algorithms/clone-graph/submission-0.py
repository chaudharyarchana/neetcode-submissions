"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # mapping old node address to new because we are visiting old so to keep track that node has been created or not
        oldToNew = {}  
        
         #dfs
        def clone(node):
            # checking if old node is already created or not
            if node in oldToNew: 
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            
            return copy

        return clone(node) if node else None


        