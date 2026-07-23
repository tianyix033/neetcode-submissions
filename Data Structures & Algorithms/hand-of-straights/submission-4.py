class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)

        for card in hand:
            if counter[card] > 0:
                start = card
                while (start - 1) in counter and counter[start - 1] > 0:
                    start -= 1
                for curr in range(start, card + 1):
                    while counter[curr] > 0:
                        for num in range(curr, curr + groupSize):
                            if counter[num] == 0:
                                return False
                            counter[num] -= 1
        return True