from collections import deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        counter = Counter(hand)
        queue = deque()
        last_num = -1
        open_groups = 0
        for card in sorted(counter):
            if (open_groups > 0 and card > last_num + 1) or open_groups > counter[card]:
                return False

            queue.append(counter[card] - open_groups)
            last_num = card
            open_groups = counter[card]

            if len(queue) == groupSize:
                open_groups -= queue.popleft()
                
        return open_groups == 0