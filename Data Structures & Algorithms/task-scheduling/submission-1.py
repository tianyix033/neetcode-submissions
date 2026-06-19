from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxf = max(counter.values())
        idle = (maxf - 1) * (n + 1)
        for count in counter.values():
            idle -= min(count, maxf - 1)
        return idle + len(tasks) if idle > 0 else len(tasks)