from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        Leng=len(nums)
        STO=1<<(Leng)
        for a in nums:
            if (a<(Leng+1)) and (a>0):
                STO|=(1<<(a-1))
        for j in range(Leng):
            if STO&1==0:
                return (j+1)
            STO=STO>>1
        return Leng+1

nums=[3,4,-1,1,2]
SOL=Solution()
Ans=SOL.firstMissingPositive(nums)
print(Ans)