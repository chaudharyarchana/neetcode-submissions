class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = {i : [] for i in range(numCourses)}
        visited = set()

        for preq,course in prerequisites:
            preqMap[course].append(preq)
        
        def dfs(course):
            if course in visited:
                return False
            if preqMap[course] == []:
                return True

            visited.add(course)
            for preq in preqMap[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            preqMap[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
           
        
        return True
        