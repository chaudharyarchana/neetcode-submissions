class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i : [] for i in range(n)}
        visited = set()
        ans = 0

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(node):
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)
        
        for node in range(n):
            if node not in visited:
                ans += 1
                dfs(node)
        
        return ans

        