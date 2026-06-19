class Solution:

    def encode(self, strs: List[str]) -> str:
        myLst = []
        for elem in strs:
            myLst.append(elem)
            myLst.append('中')            
        return ''.join(myLst)

    def decode(self, s: str) -> List[str]:
        res = s.split('中')
        res.pop()
        return res
