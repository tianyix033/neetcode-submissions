from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for num in nums:
            if mp[num] == 0:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
        try:
            return max(mp.values())
        except ValueError:
            return 0