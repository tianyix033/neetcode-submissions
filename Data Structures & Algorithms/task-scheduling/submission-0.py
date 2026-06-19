from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-freq for freq in counter.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            if heap:
                task = heapq.heappop(heap)
                if task < -1:
                    queue.append((task + 1, time + n))
            if queue and queue[0][1] == time:
                task, _ = queue.popleft()
                heapq.heappush(heap, task)
            time += 1
        return time