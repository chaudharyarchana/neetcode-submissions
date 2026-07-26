class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        visited = set()
        cycle = set()
        cycleStart = -1
        adjList = {i : [] for i in range(1, n+1)}

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node,prev):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                visited.add(node)
                return True
            visited.add(node)
            
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if dfs(nei,node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            
            return False
        
        dfs(1,-1)
        
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return[u,v]
        
        return[]
        