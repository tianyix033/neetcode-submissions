from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        heap = hand.copy()
        heapq.heapify(heap)
        counter = Counter(hand)
        while heap:
            card = heapq.heappop(heap)
            if counter[card] > 0:
                for num in range(card, card + groupSize):
                    if counter[num] == 0:
                        return False
                    counter[num] -= 1
        return True

        