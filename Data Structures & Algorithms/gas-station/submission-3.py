class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = len(gas) - 1
        end = 0
        gas_amount = gas[start] - cost[start]
        while start > end:
            if gas_amount >= 0:
                gas_amount += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                gas_amount += gas[start] - cost[start]
        return start if gas_amount >= 0 else -1
        