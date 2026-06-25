class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqsCollection = [[] for _ in range(numCourses)]
        res = []
        seen = [False] * numCourses
        for course, prereq in prerequisites:
            prereqsCollection[course].append(prereq)

        cache = set()  # any false will propogate to the top of the stack directly
        def helper(course):
            if course in cache: return True
            if seen[course]:    return False
            seen[course] = True
            for prereq in prereqsCollection[course]:
                if not helper(prereq):
                    return False
            res.append(course)
            cache.add(course)
            seen[course] = False
            return True

        for course, prereqs in enumerate(prereqsCollection):
            if not helper(course):
                return []
        return res
