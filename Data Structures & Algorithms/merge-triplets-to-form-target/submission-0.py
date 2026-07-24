class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        a_s, b_s, c_s = [], [], []
        for triplet in triplets:
            if triplet[0] == a and triplet[1] <= b and triplet[2] <= c:
                a_s.append(triplet)
            if triplet[1] == b and triplet[0] <= a and triplet[2] <= c:
                b_s.append(triplet)
            if triplet[2] == c and triplet[0] <= a and triplet[1] <= b:
                c_s.append(triplet)
        return bool(a_s and b_s and c_s)
        
            
        