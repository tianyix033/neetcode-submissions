class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        num_prereqs = [0] * numCourses
        dependencies = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            num_prereqs[course] += 1
            dependencies[prereq].append(course)

        stack = []
        for course, num in enumerate(num_prereqs):
            if num == 0:
                stack.append(course)

        res = []
        while stack:
            course = stack.pop()
            res.append(course)
            for dependent in dependencies[course]:
                num_prereqs[dependent] -= 1
                if num_prereqs[dependent] == 0:
                    stack.append(dependent)

        
        return res if len(res) == numCourses else []
        