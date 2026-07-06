class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        MAPPING = [0, 0, ('a', 'b', 'c'), ('d', 'e', 'f'), 
        ('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), 
        ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z')]

        res = []
        curr = [""]   # all permutations at current position
        for digit in digits:
            for curr_word in curr:
                for curr_letter in MAPPING[int(digit)]:
                    res.append(curr_word + curr_letter)
            curr = res
            res = []

        return curr