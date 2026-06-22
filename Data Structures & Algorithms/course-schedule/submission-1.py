class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for course, prereq in prerequisites:
            if course not in prereqs:
                prereqs[course] = []
            prereqs[course].append(prereq)

        seen = set()
        done = set()
        def dfs(course):
            if (course not in prereqs) or (course in done):
                return True
            for prereq in prereqs[course]:
                if prereq in seen:
                    return False
                else:
                    seen.add(prereq)
                    res = dfs(prereq)
                    seen.remove(prereq)
                    if res == False:
                        return False
            done.add(course)
            return True
        
        for i in range(numCourses):
            if i not in done:
                seen.add(i)
                if dfs(i) == False:
                    return False
                seen.remove(i)

        return True