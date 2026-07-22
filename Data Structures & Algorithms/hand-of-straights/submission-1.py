from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        counter = Counter(hand)
        for card in hand:
            if counter[card] > 0:
                for num in range(card, card + groupSize):
                    if counter[num] == 0:
                        return False
                    counter[num] -= 1
        return True

        