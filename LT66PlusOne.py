from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Leng=len(digits)
        for i in range(Leng-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        return [1]+digits


Dig=[9,8,9]
Ans=Solution().plusOne(Dig)
print(Ans)