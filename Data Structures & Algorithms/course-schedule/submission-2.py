class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_count = {i: 0 for i in range(numCourses)}
        dependencies = {i: [] for i in range(numCourses)}
        for dependent, prereq in prerequisites:
            prereq_count[dependent] += 1
            dependencies[prereq].append(dependent)

        stack = []
        for prereq, count in prereq_count.items():
            if count == 0:
                stack.append(prereq)
        while stack:
            prereq = stack.pop()
            for dependent in dependencies[prereq]:
                prereq_count[dependent] -= 1
                if prereq_count[dependent] == 0:
                    stack.append(dependent)
        
        for count in prereq_count.values():
            if count > 0:
                return False

        return True