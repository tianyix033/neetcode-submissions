class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        MAPPING = [0, 0, ('a', 'b', 'c'), ('d', 'e', 'f'), 
        ('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), 
        ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z')]

        res = []
        curr = []   # list representation of current word
        def add_letter(pos):
            if pos == len(digits):
                res.append("".join(curr))
                return
            for curr_letter in MAPPING[int(digits[pos])]:
                curr.append(curr_letter)
                add_letter(pos + 1)
                curr.pop()

        add_letter(0)
        return res
