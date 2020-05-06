from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        MaxLeng,Leng,j=0,len(nums),0
        for i in range(Leng):
            MaxLeng=max(MaxLeng,j+nums[j])
            if MaxLeng+1>=Leng:return True
            if j<MaxLeng:
                j+=1
            else:
                return False


nums=[3,2,1,0,4]
nums=[2,3,1,1,4]
SOL=Solution()
Ans=SOL.canJump(nums)
print(Ans)