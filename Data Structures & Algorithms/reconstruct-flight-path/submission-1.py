class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = {src: [] for src,des in tickets}

        for src,des in tickets:
            adjList[src].append(des)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adjList:
                return False
            
            temp = list(adjList[src])
            for i,des in enumerate(temp):
                adjList[src].pop(i)
                res.append(des)

                if dfs(des):
                    return True
                
                adjList[src].insert(i,des)
                res.pop()
            
        dfs("JFK")
        return res
        