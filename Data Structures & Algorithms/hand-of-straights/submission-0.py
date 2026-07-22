class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        first_pos = {}
        for i, card in enumerate(hand):
            if card not in first_pos:
                first_pos[card] = i
        for card in first_pos:
            while first_pos[card] != -1:
                for num in range(card, card + groupSize):
                    if num not in first_pos or first_pos[num] == -1:
                        return False
                    if first_pos[num] + 1 < len(hand) and hand[first_pos[num] + 1] == num:
                        first_pos[num] += 1
                    else:
                        first_pos[num] = -1
        return True

        