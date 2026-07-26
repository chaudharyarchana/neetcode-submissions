class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = {i: [] for i in range(numCourses)}
        ans = []
        visiting = set()

        for course, preq in prerequisites:
            preqMap[course].append(preq)

        def dfs(course):
            # Already processed
            if preqMap[course] == [-1]:
                return True

            # Cycle detected
            if course in visiting:
                return False

            visiting.add(course)

            for preq in preqMap[course]:
                if not dfs(preq):
                    return False

            visiting.remove(course)
            preqMap[course] = [-1]   # Mark as processed
            ans.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return ans