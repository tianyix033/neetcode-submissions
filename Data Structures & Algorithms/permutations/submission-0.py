class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numset = set(nums)
        res = []
        sublist = []
        def helper():
            if not numset:
                res.append(sublist.copy())
                return
            iterator = numset.copy()
            for num in iterator:
                numset.remove(num)
                sublist.append(num)
                helper()
                sublist.pop()
                numset.add(num)

        helper()
        return res
