class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        seen = [False] * n
        max_seen = -1

        for i in range(n):
            if i > max_seen:
                curr = i
                gas_amount = 0
                while True:
                    max_seen = max(max_seen, curr)
                    gas_amount += gas[curr] - cost[curr]
                    if gas_amount < 0:
                        break
                    elif (curr + 1) % n == i:
                            return i
                    curr = (curr + 1) % n

        return -1
