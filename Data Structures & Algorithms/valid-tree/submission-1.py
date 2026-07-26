class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(n)}
        visited = set()
        
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for n in adjList[node]:
                if n == prev:
                    continue
                if not dfs(n,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n


        