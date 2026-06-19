from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = deque()
        seen = set([0])
        queue.append(0)
        num_of_coins = 0
        while queue:
            num_of_coins += 1
            num_iters = len(queue)
            for iter in range(num_iters):
                curr_sum = queue.popleft()
                for coin in coins:
                    new_sum = curr_sum + coin
                    if new_sum == amount:
                        return num_of_coins
                    if new_sum < amount and new_sum not in seen:
                        seen.add(new_sum)
                        queue.append(new_sum)

        return -1
            