from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                counter = Counter(s[i:j])
                if counter:
                    most_common = counter.most_common(1)[0][1]
                    chars_to_replace = (j - i) - most_common
                    if chars_to_replace <= k:
                        res = max(res, (j - i))
        return res