class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        a_s, b_s, c_s = False, False, False
        for triplet in triplets:
            if triplet[0] == a and triplet[1] <= b and triplet[2] <= c:
                a_s = True
            if triplet[1] == b and triplet[0] <= a and triplet[2] <= c:
                b_s = True
            if triplet[2] == c and triplet[0] <= a and triplet[1] <= b:
                c_s = True
        return a_s and b_s and c_s
        
            
        