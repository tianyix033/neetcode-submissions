class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        curr_dict = {}
        res = 0
        curr_max = 0
        while right < len(s) and left < len(s):
            length = right - left + 1
            right_char = s[right]
            if right_char not in curr_dict:
                curr_dict[right_char] = 0
            curr_dict[right_char] += 1
            curr_max = max(curr_dict[right_char], curr_max)
            if length - curr_max <= k:
                res = max(res, length)
            else:
                # Critical: We do not need to recalculate curr_max
                # because we only care about the maximum curr_max;
                # if it goes down, ain't gonna use that window anyways
                left_char = s[left]
                left += 1
                curr_dict[left_char] -= 1
            right += 1
        return res




