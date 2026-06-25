class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqsCollection = [[] for _ in range(numCourses)]
        res = []
        seen = [False] * numCourses
        taken = set()
        for course, prereq in prerequisites:
            prereqsCollection[course].append(prereq)

        def helper(course):
            if seen[course]:    return False
            seen[course] = True
            for prereq in prereqsCollection[course]:
                if not helper(prereq):
                    return False
            if course not in taken:
                res.append(course)
                taken.add(course)
            seen[course] = False
            return True

        for course, prereqs in enumerate(prereqsCollection):
            if not helper(course):
                return []
        return res
