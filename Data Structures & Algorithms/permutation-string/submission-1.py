class Solution:
    def dict_is_zero(self, dict):
        for val in dict.values():
            if val != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        left = 0
        right = len(s1)
        mydict = {chr(ord('a') + i) : 0 for i in range(26)}
        for char in s1:
            mydict[char] += 1
        for i in range(len(s1)):
            mydict[s2[i]] -= 1
        # print(mydict)
        while ((not self.dict_is_zero(mydict)) and (right < len(s2))):
            # print(mydict)
            mydict[s2[left]] += 1
            mydict[s2[right]] -= 1
            left += 1
            right += 1
        return self.dict_is_zero(mydict)

        

        
        